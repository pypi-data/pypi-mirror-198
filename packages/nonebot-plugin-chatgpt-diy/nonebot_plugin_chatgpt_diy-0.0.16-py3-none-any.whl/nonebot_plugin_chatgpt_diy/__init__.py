from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import MessageEvent, PrivateMessageEvent, PRIVATE, Message, MessageSegment, Bot
import nonebot
from nonebot.params import ArgStr, CommandArg, EventPlainText
from nonebot import on_message, on_command
from nonebot.message import handle_event
from pathlib import Path
from transformers import GPT2TokenizerFast
import os
import json
import asyncio
import time

from .model import get_chat_response, get_response
from .config import Config

# 文档操作----------------------------------------------------------------------------


STATE_OK = True
STATE_ERROR = False


def write_data(path: Path, data: list) -> bool:
    try:
        if data:
            flag = 0
            for info in data:
                if flag == 0:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(' '.join(info))
                    flag = 1
                elif flag == 1:
                    with open(path, 'a', encoding='utf-8') as f:
                        f.write('\n' + (' '.join(info)))
        else:
            with open(path, 'w') as f:
                f.write('')
        return STATE_OK
    except Exception as e:
        logger.error(e)
        return STATE_ERROR


def read_data(path: Path) -> (bool, list):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.readlines()
        infos = [x.split() for x in data]

        return STATE_OK, infos
    except Exception as e:
        logger.error(e)
        return STATE_ERROR, []

# 配置地址----------------------------------------------------------


global_config = nonebot.get_driver().config
gpt3_config = Config.parse_obj(global_config.dict())
chatgpt3_path = gpt3_config.chatgpt3_path

api_key = gpt3_config.api_key
if not api_key:
    logger.error("未设置api_key参数，插件无法正常运行")
    raise ValueError("未设置api_key参数，插件无法正常运行")


if chatgpt3_path == Path():
    chatgpt3_path = chatgpt3_path / \
        os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(chatgpt3_path):
    os.makedirs(chatgpt3_path)
    logger.info(f"新建文件夹成功，设置当前储存路径为{chatgpt3_path}")

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# 注册响应器------------------------------------------------------------


gpt3 = on_message(permission=PRIVATE, priority=10)
set_background = on_command("添加背景", priority=5, block=True)
choice_background = on_command("选择背景", priority=5, block=True)
# delete_background = on_command("删除背景", priority=5, block=True)
chat_gpt3 = on_command("开始聊天", priority=4, block=True, aliases={"开始对话"})


# 添加背景---------------------------------------------------------------------------------------------

@set_background.handle()
async def _(state: T_State, args: Message = CommandArg()):
    msg = args.extract_plain_text().strip()
    if msg:
        state["bot_name"] = msg


@set_background.got("bot_name", prompt="请输入您要添加背景的机器人的名称，如 上官雨筝")
async def _(state: T_State, bot_name: str = ArgStr("bot_name")):
    await asyncio.sleep(1)
    await set_background.send(f"当前设置机器人名称为{bot_name}")


@set_background.got("master_name", prompt="请输入当前您在背景中的名称")
async def _(state: T_State, master_name: str = ArgStr("master_name")):
    await asyncio.sleep(1)
    state["master_name"] = master_name
    await set_background.send(f"当前您的名称设置为{master_name}")


@set_background.got("bot_info", prompt="请输入当前您设定的聊天背景,尽量注意标点符号，并且限制字数为200字")
async def _(event: MessageEvent, state: T_State, bot_info: str = ArgStr("bot_info")):
    await asyncio.sleep(1)
    if bot_info in ["算了", "取消"]:
        await set_background.finish("已取消当前操作")
    if len(bot_info) > 200:
        await set_background.finish("bot_info", prompt="输入字数超过200，请重新输入")
    background = {
        "bot_name": str(state["bot_name"]),
        "master_name": str(state["master_name"]),
        "bot_info": str(bot_info),
        "is_default": False
    }
    if os.path.exists(
        os.path.join(
            chatgpt3_path,
            f"{event.user_id}_background.json")):
        with open(os.path.join(chatgpt3_path, f"{event.user_id}_background.json"), "r", encoding="utf-8") as f:
            backgrounds = json.load(f)
    else:
        backgrounds = []
    bot_names = [x["bot_name"] for x in backgrounds]
    if str(state["bot_name"]) in bot_names:
        backgrounds.pop(bot_names.index(str(state["bot_name"])))
        await asyncio.sleep(0.5)
    backgrounds.append(background)
    with open(os.path.join(chatgpt3_path, f"{event.user_id}_background.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(backgrounds, ensure_ascii=False))
    await set_background.finish("添加背景成功！")


# 选择背景--------------------------------------------------------------------------------------------


@choice_background.handle()
async def _(event: MessageEvent, state: T_State):
    if os.path.exists(
        os.path.join(
            chatgpt3_path,
            f"{event.user_id}_background.json")):
        with open(os.path.join(chatgpt3_path, f"{event.user_id}_background.json"), "r", encoding="utf-8") as f:
            backgrounds = json.load(f)
            state["backgrounds"] = backgrounds
            res = "您当前保存的背景有:\n"
            for i in range(len(backgrounds)):
                res += f"{i}. {backgrounds[i]['bot_name']}\n"
            await choice_background.send(res)
            await asyncio.sleep(0.5)
    else:
        await choice_background.finish("您暂未添加背景，请先进行添加")


@choice_background.got("num", prompt="请输入您要选择的背景序号")
async def _(event: MessageEvent, state: T_State, num: str = ArgStr("num")):
    try:
        num = int(num)
    except BaseException:
        await choice_background.reject_arg("num", "输入数字有误，请重新输入")
    backgrounds = state["backgrounds"]
    for i in range(len(backgrounds)):
        if i == num:
            backgrounds[i]["is_default"] = True
        else:
            backgrounds[i]["is_default"] = False
    with open(os.path.join(chatgpt3_path, f"{event.user_id}_background.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(backgrounds, ensure_ascii=False))
    res = f"成功选择当前默认背景为:\n{backgrounds[num]['bot_name']}\n\n背景如下:\n{backgrounds[num]['bot_info']}"
    await asyncio.sleep(1)
    await choice_background.finish(res)

# 私聊会话---------------------------------------------------------------------------------------------


@gpt3.handle()
async def _(bot:Bot, event: PrivateMessageEvent, msg: Message = EventPlainText()):
    prompt = "请对我的命令做自然语言处理，判断我的意图，并将原始命令转换成如下格式之一，其中引号内为转换后命令的格式，括号内的部分为可选参数，每一个命令都附带有3个示例，你可以根据示例进行学习。但是请注意，并不是每一个命令都可以被转化为相应的命令，在你无法做出处理时请回复”抱歉，我没有找到相应的命令“。转换后的命令格式如下：" \
             "\n1.“xdu功能订阅 （功能名称）”" \
             "\n示例1：xdu功能订阅" \
             "\n示例2：xdu功能订阅 体育打卡" \
             "\n示例3：xdu功能订阅 课表提醒" \
             "\n2.“xdu功能退订 （功能名称）”" \
             "\n示例1：xdu功能退订" \
             "\n示例2：xdu功能退订 体育打卡" \
             "\n示例3：xdu功能退订 课表提醒" \
             "\n3. “体育打卡查看”" \
             "\n示例1：体育打卡查看" \
             "\n示例2：体育打卡查询" \
             "\n4.“课表查询”" \
             "\n示例1：课表查询" \
             "\n示例2：我的课表" \
             "\n5.“更新课表”" \
             "\n示例1：更新课表" \
             "\n示例2：课表更新" \
             "\n6. “空闲教室查询 （教学楼） （日期）”" \
             "\n示例1：空闲教室查询" \
             "\n示例2：空闲教室查询 信远教学楼I区 今天" \
             "\n示例3：空闲教室查询 信远教学楼II区" \
             "\n示例4：空闲教室查询 B教学楼 下周四" \
             "\n7. “添加停止教室 （教室号）”" \
             "\n示例1：添加停止教室" \
             "\n示例2：添加停止教室 B-108" \
             "\n示例3：添加停止教室 信远I-302" \
             "\n8.“成绩查询 （学期）”" \
             "\n示例1：我的成绩" \
             "\n示例2：我的成绩 上学期" \
             "\n示例3：成绩查询" \
             "\n9.“青年大学习”" \
             "\n示例1：青年大学习" \
             "\n示例2：未完成学习" \
             "\n10： “提醒 （事件） （日期）”" \
             "\n示例1：提醒 青年大学习 下周一" \
             "\n示例2：提醒 通信原理考试 下周二" \
             "\n示例3：提醒 见老师 今天" \
             "\n\n你只需要给出命令，不需要说多余的话，切记，不用说其他的话，只需要给出格式命令文字本身" \
             "\n你只需要给出命令，不需要说多余的话，切记，不用说其他的话，只需要给出格式命令文字本身"
    cmd = f"需要被转化的命令为:{msg}"
    content = [{"role": "user", "content": prompt}, {"role":"assistant","content":"我明白了，请告诉我您需要执行哪个命令。"},{"role": "user", "content": cmd}]
    res = await get_response(content, api_key)
    print(res)
    msg_event = MessageEvent(time=int(time.time()), self_id=event.self_id, post_type="message", sub_type="friend",
                             user_id=event.user_id, message_type="private", message_id=event.message_id,
                             message=[{"type": "text", "data": {"text": res}}],
                             original_message=[{"type": "text", "data": {"text": res}}],
                             raw_message=res, font=0,
                             sender={"user_id": event.sender.user_id, "nickname": event.sender.nickname,
                                     "sex": event.sender.sex, "age": event.sender.age, "card": event.sender.card,
                                     "area": event.sender.area, "level": event.sender.level, "role": event.sender.role,
                                     "title": event.sender.title}, to_me=event.to_me, reply=event.reply,
                             target_id=event.self_id)
    # if res != "我找不到相应的命令":
    #     asyncio.create_task(handle_event(bot, msg_event))
    # else:
    #     user_id = str(event.user_id)
    #     if os.path.exists(
    #         os.path.join(
    #             chatgpt3_path,
    #             f"{user_id}_background.json")):
    #         with open(os.path.join(chatgpt3_path, f"{user_id}_background.json"), "r", encoding="utf-8") as f:
    #             backgrounds_json = json.load(f)
    #         flag = 0
    #         for background in backgrounds_json:
    #             if background["is_default"]:
    #                 flag = 1
    #                 background_json = background
    #         if flag == 0:
    #             await gpt3.finish("您暂未选择背景，请先选择")
    #     else:
    #         await gpt3.finish("您暂未添加背景，请先添加背景。")
    #     if msg in ["重置会话", "重置聊天", "聊天重置", "会话重置"]:
    #         conversation = []
    #         await gpt3.finish(".")
    #     bot_name = background_json["bot_name"]
    #     background = background_json["bot_info"]
    #     master_name = background_json["master_name"]
    #     start_sequence = f"\n{bot_name}:"
    #     restart_sequence = f"\n{master_name}: "
    #     if os.path.exists(
    #         os.path.join(
    #             chatgpt3_path,
    #             f"{user_id}_{bot_name}_conversation.txt")):
    #         with open(os.path.join(chatgpt3_path, f"{user_id}_{bot_name}_conversation.txt"), "r", encoding="utf-8") as f:
    #             try:
    #                 conversation = eval(f.read().replace("\\\\", "\\"))
    #             except Exception as e:
    #                 logger.error(e)
    #                 conversation = []
    #     else:
    #         f = open(
    #             os.path.join(
    #                 chatgpt3_path,
    #                 f"{user_id}_{bot_name}_conversation.txt"),
    #             "w",
    #             encoding="utf-8")
    #         f.close()
    #         conversation = []
    #     if len(conversation):
    #         prompt = background + "".join(conversation) + msg
    #         len_prompt = len(tokenizer.encode(prompt))
    #         while len(conversation) > 12 or len_prompt > 2047:
    #             conversation.pop(0)
    #             prompt = background + "".join(conversation) + msg
    #             len_prompt = len(tokenizer.encode(prompt))
    #     else:
    #         prompt = background + restart_sequence + msg + start_sequence
    #     await asyncio.sleep(2)
    #
    #     resp, flag = get_chat_response(
    #         api_key, prompt, start_sequence, bot_name, master_name)
    #     resp = resp.replace("&#91;", "[").replace("&#93;", "]")
    #     if not resp:
    #         resp = "..."
    #     if flag:
    #         conversation.append(f"{msg}{start_sequence}{resp}{restart_sequence}")
    #         with open(os.path.join(chatgpt3_path, f"{user_id}_{bot_name}_conversation.txt"), "w", encoding="utf-8") as f:
    #             f.write(str(conversation).replace("\\", "\\\\"))
    #         await gpt3.finish(resp)
    #     else:
    #         logger.error(resp)
    #         await gpt3.finish("我没听清你说什么，能再说一次吗")


@chat_gpt3.handle()
async def _(event: MessageEvent, state: T_State):
    state["user_id"] = str(event.user_id)
    user_id = str(event.user_id)
    if os.path.exists(
            os.path.join(
                chatgpt3_path,
                f"{user_id}_background.json")):
        with open(os.path.join(chatgpt3_path, f"{user_id}_background.json"), "r", encoding="utf-8") as f:
            backgrounds_json = json.load(f)
        flag = 0
        for background in backgrounds_json:
            if background["is_default"]:
                flag = 1
                background_json = background
        if flag == 0:
            await gpt3.finish("您暂未选择背景，请先选择背景")
    else:
        await gpt3.finish("您暂未使用背景，请先添加背景")

    state["bot_name"] = background_json["bot_name"]
    state["background"] = background_json["bot_info"]
    state["master_name"] = background_json["master_name"]
    if os.path.exists(
            os.path.join(
                chatgpt3_path,
                f"{user_id}_{background_json['bot_name']}_conversation.txt")):
        with open(os.path.join(chatgpt3_path, f"{user_id}_{background_json['bot_name']}_conversation.txt"), "r", encoding="utf-8") as f:
            try:
                conversation = eval(f.read().replace("\\\\", "\\"))
            except Exception as e:
                logger.error(e)
                conversation = []
    else:
        f = open(
            os.path.join(
                chatgpt3_path,
                f"{user_id}_{background_json['bot_name']}_conversation.txt"),
            "w",
            encoding="utf-8")
        f.close()
        conversation = []

    state["conversation"] = conversation
    await chat_gpt3.send("聊天开始...")


@chat_gpt3.got("prompt")
async def _(event: MessageEvent, state: T_State, msg: Message = ArgStr("prompt")):
    if msg in ["算了", "取消", "结束对话", "对话结束", "聊天结束", "结束聊天"]:
        await chat_gpt3.finish("聊天结束")
    bot_name = state["bot_name"]
    master_name = state["master_name"]
    conversation = state["conversation"]
    if msg in ["重置会话", "重置聊天", "聊天重置", "会话重置"]:
        conversation = []
        await chat_gpt3.reject_arg("prompt", prompt="会话已重置")
    background = state["background"]
    start_sequence = f"\n{bot_name}:"
    restart_sequence = f"\n{master_name}: "

    if len(conversation):
        prompt = background + "".join(conversation) + msg
        len_prompt = len(tokenizer.encode(prompt))
        while len(conversation) > 12 or len_prompt > 2047:
            conversation.pop(0)
            prompt = background + "".join(conversation) + msg
            len_prompt = len(tokenizer.encode(prompt))
    else:
        prompt = background + restart_sequence + msg + start_sequence
    await asyncio.sleep(2)

    resp, flag = get_chat_response(
        api_key, prompt, start_sequence, bot_name, master_name)
    resp = resp.replace("&#91;", "[").replace("&#93;", "]")
    if not resp:
        resp = "..."
    if flag:
        conversation.append(f"{msg}{start_sequence}{resp}{restart_sequence}")
        with open(os.path.join(chatgpt3_path, f"{event.user_id}_{bot_name}_conversation.txt"), "w", encoding="utf-8") as f:
            f.write(str(conversation).replace("\\", "\\\\"))
        if isinstance(event, PrivateMessageEvent):
            await chat_gpt3.reject_arg("prompt", prompt=resp)
        else:
            await chat_gpt3.reject_arg("prompt", prompt=MessageSegment.reply(event.message_id)+resp)
    else:
        logger.error(resp)
        await chat_gpt3.reject_arg("prompt", prompt="我刚刚没听清你说什么，能再说一次吗")


