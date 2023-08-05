# 插件：随机点名 v1.0
# 作者：青木

from pathlib import Path
import random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.params import  CommandArg

roll_info_path = Path.cwd() / "data" / "roll_call"
if not roll_info_path.exists(): # 如果不存在就创建一个
    roll_info_path.mkdir(parents=True) # 创建文件夹

# 读取roll_info_path 文件夹下的所有文件
roll_info_list = list(roll_info_path.glob("*.txt"))
# 读取文件内容
def read_roll_info(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        roll_info = f.read().splitlines()
    return roll_info

roll_help= """
随机点名
用法：
    1.随机点名 文件名；
    2.查询文件列表；
"""
roll_call = on_command("roll_call", aliases={"随机点名"}, priority=5, block=True)
roll_call_list = on_command("roll_call_list", aliases={"查询文件列表"}, priority=5, block=True)
roll_call_help = on_command("roll_call_help", aliases={"点名帮助","help"}, priority=5, block=True)

@roll_call.handle()
async def _(event: Event, args: Message = CommandArg()):
    args = args.extract_plain_text().split()
    if len(args) == 0:
        await roll_call.finish("请输入点名文件名")
    file_name = args[0]
    roll_info = read_roll_info(roll_info_path / f"{file_name}.txt")
    roll_name = random.choice(roll_info)
    await roll_call.finish(MessageSegment.at(event.get_user_id()) + f"\n{roll_name}")

@roll_call_list.handle()
async def _(event: Event, args: Message = CommandArg()):
    args = args.extract_plain_text().split()
    if len(args) == 0:
        roll_info_list = list(roll_info_path.glob("*.txt"))
        roll_info_list = [i.stem for i in roll_info_list]
        await roll_call_list.finish(f"点名文件列表：\n{roll_info_list}")
    else:
        await roll_call_list.finish("参数错误")

@roll_call_help.handle()
async def _(event: Event, args: Message = CommandArg()):
    args = args.extract_plain_text().split()
    if len(args) == 0:
        await roll_call_help.finish(roll_help)
    else:
        await roll_call_help.finish("参数错误")