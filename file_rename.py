"""
Name: file_rename.py
Description: 批量重命名日志文件
Version: 1.0.0
Created_at: 2025.05.04
Updated_at: 2025.05.04
Usage: python file_rename.py [folder]
Author: Huang Daojin

编写一个Python脚本，批量重命名指定文件夹中的所有文件。将如“世赛网管精英班训练日志-教练-黄道金-2025.04.01-自动化-编写第一个Python程序.pdf”的文件重命名为“网络系统管理项目2025年04月01日教练日志-黄道金.pdf”。源文件的文件名是有规律的6个小结组成，分别是“开头”-“角色”-“姓名”-“日期”-“模块”-“任务”.“扩展名”。重命名后的文件名中，“网络系统管理项目”是新的固定开头，“2025年04月01日”是根据原文件名中的日期“2025.04.01”部分提取转换而来，“教练日志”是根据原文件名中的“角色”提取转换而来，“黄道金”是根据原文件名中的“姓名”提取而来，保留原来的文件扩展名。其他新文件名中不包含的小结就舍弃了。

"""

from pathlib import Path
import argparse

def parse_filename(filename):
    """解析文件名，提取角色、姓名、日期和扩展名"""
    p = Path(filename)
    name, ext = p.stem, p.suffix
    parts = name.split('-')
    if len(parts) < 6:
        return None
    return {
        'role': parts[1].strip(),
        'name': parts[2].strip(),
        'date': parts[3].strip(),
        'ext': ext
    }

def format_date(d):
    """将'YYYY.MM.DD'格式转为'YYYY年MM月DD日'"""
    try:
        y, m, day = d.split('.')
        return f"{y}年{m}月{day}日"
    except ValueError:
        return d

def get_role_suffix(role):
    """根据角色生成日志后缀"""
    if role == "教练":
        return "教练日志"
    if role == "选手":
        return "学生日志"
    return f"{role}日志"

def rename_files(folder):
    """遍历目录，按规则重命名所有文件"""
    folder = Path(folder)
    if not folder.is_dir():
        print(f"错误：{folder} 不是有效目录")
        return
    for src in folder.iterdir():
        if not src.is_file():
            continue
        info = parse_filename(src.name)
        if not info:
            print(f"跳过：{src.name}（格式不符）")
            continue
        new_name = (
            "网络系统管理项目"
            + format_date(info['date'])
            + get_role_suffix(info['role'])
            + "-"
            + info['name']
            + info['ext']
        )
        dst = folder / new_name
        try:
            src.rename(dst)
            print(f"{src.name} -> {new_name}")
        except Exception as e:
            print(f"重命名失败：{src.name}，原因：{e}")

def main():
    parser = argparse.ArgumentParser(description="批量重命名日志文件")
    parser.add_argument(
        "folder",
        nargs="?",
        default=Path.cwd(),
        help="要处理的文件夹路径，缺省为当前目录"
    )
    args = parser.parse_args()
    rename_files(args.folder)

if __name__ == "__main__":
    main()
