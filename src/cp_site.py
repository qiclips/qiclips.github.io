import os
import shutil


def copy_all_files(source_dir, destination_dir):
    """
    复制指定源目录下的所有文件和文件夹到目标目录。

    :param source_dir: 源目录的路径
    :param destination_dir: 目标目录的路径
    """
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_file_path, source_dir)
                target_file_path = os.path.join(destination_dir, relative_path)
                target_sub_dir = os.path.dirname(target_file_path)
                if not os.path.exists(target_sub_dir):
                    os.makedirs(target_sub_dir)
                shutil.copy2(source_file_path, target_file_path)
                print(f"Copied {source_file_path} to {target_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def copy_html_and_xml_files(source_dir, destination_dir):
    """
    复制指定源目录下的所有 HTML 和 XML 文件到目标目录，忽略 assets 文件夹。

    :param source_dir: 源目录的路径
    :param destination_dir: 目标目录的路径
    """
    # 确保目标目录存在
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    cp_files = []
    # 遍历源目录下的所有文件和文件夹
    for root, dirs, files in os.walk(source_dir):
        # 跳过包含 assets 的目录
        if 'assets' in root.split(os.sep):
            continue
        for file in files:
            if file.endswith(('.html', '.xml')):
                # 构建源文件的完整路径
                source_file = os.path.join(root, file)
                # 构建目标文件的完整路径
                relative_path = os.path.relpath(source_file, source_dir)
                destination_file = os.path.join(destination_dir, relative_path)
                # 确保目标文件所在的目录存在
                destination_file_dir = os.path.dirname(destination_file)
                if not os.path.exists(destination_file_dir):
                    os.makedirs(destination_file_dir)
                # 复制文件
                try:
                    cp_file = shutil.copy2(source_file, destination_file)
                    cp_files.append(cp_file)
                    print(f"Copied {source_file} to {source_file}")
                except Exception as e:
                    print(f"复制文件 {source_file} 到 {destination_file} 时出错: {e}")
    return cp_files


def replace_text_in_files(locale, cp_files, destination_directory):
    """
    替换文件中的特定文本，主要是在文件路径前添加 /en 前缀

    :param locale: 语言
    :param cp_files: 要处理的文件列表
    :param destination_directory: 目标目录路径
    :return: 无
    """
    # 替换文件相对目录
    replace_texts = []
    for cp_file in cp_files:
        replace_text = cp_file.replace(destination_directory, '').replace('index.html', '').replace('\\', '/')
        replace_texts.append(replace_text)
        print(cp_file, '->', replace_text)

    for cp_file in cp_files:
        # 读取文件内容并进行替换
        with open(cp_file, 'r', encoding='utf-8') as f:
            content = f.read()
            for replace_text in replace_texts:
                content = content.replace('\"' + replace_text + '\"', '\"/'+locale + replace_text + '\"')
                if cp_file.endswith('sitemap.xml'):
                    content = content.replace('<loc>' + replace_text + '</loc>', '<loc>/en' + replace_text + '</loc>')
            # 将替换后的内容写回文件
            with open(cp_file, 'w', encoding='utf-8') as f:
                f.write(content)


def main(locale, work_dir= '../'):
    # 获取当前运行文件的目录
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    # 修改工作目录为运行文件的目录
    os.chdir(current_file_dir)

    # 设置源目录和目标目录
    source_directory = os.path.abspath('../_site')
    destination_directory = os.path.abspath('../_output/'+locale)
    if locale == 'zh-CN':
        copy_all_files(source_directory, destination_directory)
        return
    # 其他语言特殊处理
    # 调用函数进行文件复制
    cp_files = copy_html_and_xml_files(source_directory, destination_directory)
    # cp_files = []
    # # 遍历源目录下的所有文件和文件夹
    # for root, dirs, files in os.walk(destination_directory):
    #     for file in files:
    #         if file.endswith(('.html', '.xml')):
    #             # 构建源文件的完整路径
    #             source_file = os.path.join(root, file)
    #             cp_files.append(source_file)
    # 调用函数进行文本替换
    replace_text_in_files(locale,cp_files, destination_directory)

if __name__ == "__main__":
    main('zh-CN')

    
        


