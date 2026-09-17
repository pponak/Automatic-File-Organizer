from pathlib import Path

# 根据文件后缀进行分类，接受一个 Path 对象作为参数
def get_category(file_path):
    suffix = file_path.suffix.lower()
    
    if suffix == ".pdf":
        return "PDF"
    elif suffix in [".jpg", ".png"]:
        return "图片"
    elif suffix == ".xlsx":
        return "Excel"
    else:
        return "其他"
    
# 整理文件，接受一个 Path 对象和一个基准文件夹作为参数
def organize_file(file_path, base_folder):
    print(f"文件名：{file_path.name}")
    print(f"后缀：{file_path.suffix}")
    print(f"路径：{file_path}")
    
    # 根据文件后缀进行分类
    category = get_category(file_path)
    print(f"分类：{category}")
    
    ## 创建分类文件夹
    category_folder = base_folder / "整理结果" / category
    ### 创建目录，如果目录已存在则不会报错
    category_folder.mkdir(parents=True, exist_ok=True)
    
    ## 文件移动到分类文件夹
    target = category_folder / file_path.name
    ### 检查目标文件是否已存在
    if target.exists():
        print(f"目标文件已存在，跳过移动：{target}")
        return
    ### rename() 方法用于移动文件
    try:
        file_path.rename(target)
    except PermissionError:
        print(f"没有权限移动文件：{file_path.name}")
    except FileNotFoundError:
        print(f"文件不存在，无法移动：{file_path.name}")
    else:
        print(f"已将{file_path.name}移动到{category_folder}")
    
    print(f"分类目录：{category_folder}")
    print()

# 主程序入口
folder_txt = input("请输入待整理目录路径：").strip()
if not folder_txt:
    print("路径不能为空")
else:
    folder = Path(folder_txt)

    # 扫描当前文件夹中的所有文件，并进行整理
    ## 检查目录是否存在
    if not folder.exists():
        print(f"目录不存在：{folder}")
    elif not folder.is_dir():
        print(f"这不是目录：{folder}")
    else:
        print(f"正在扫描目录：{folder}")
        ## 遍历目录中的所有文件
        for item in folder.iterdir():
            if item.is_file():
                ## 绕过当前脚本文件，避免移动自身
                if item.name == "scanner.py":
                    continue
                
                organize_file(item, folder)
        
