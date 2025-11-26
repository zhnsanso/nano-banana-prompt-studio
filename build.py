"""
Nano Banana 提示词生成器 - 打包脚本
将应用打包成独立的可执行文件

使用方法:
    python build.py
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path


APP_NAME = 'NanoBananaPromptTool'


def clean_build_dirs():
    """清理之前的构建目录"""
    dirs_to_clean = ['build', 'dist', 'output']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"清理目录: {dir_name}")
            shutil.rmtree(dir_name)


def clean_temp_files():
    """清理打包产生的临时文件"""
    print("\n清理临时文件...")
    
    # 删除 build 和 dist 目录
    for dir_name in ['build', 'dist']:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  已删除: {dir_name}/")
    
    # 删除 .spec 文件
    for spec_file in Path('.').glob('*.spec'):
        spec_file.unlink()
        print(f"  已删除: {spec_file}")


def install_pyinstaller():
    """确保 PyInstaller 已安装"""
    try:
        import PyInstaller
        print(f"PyInstaller 已安装: {PyInstaller.__version__}")
    except ImportError:
        print("正在安装 PyInstaller...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])


def build_exe():
    """使用 PyInstaller 构建可执行文件"""
    print("\n开始构建可执行文件...")
    
    # PyInstaller 参数
    pyinstaller_args = [
        'src/main.py',                          # 入口文件
        f'--name={APP_NAME}',                   # 生成的exe名称
        '--windowed',                            # 无控制台窗口 (GUI应用)
        '--onedir',                              # 打包成目录形式 (比单文件更快启动)
        '--noconfirm',                           # 不确认覆盖
        '--clean',                               # 清理临时文件
        '--icon=images/logo.png',               # 应用图标
        
        # 添加数据文件
        '--add-data=src/config;config',          # 配置目录
        '--add-data=src/presets;presets',        # 预设目录
        '--add-data=images/logo.png;images',     # logo图片
        
        # 隐藏导入（确保所有模块都被包含）
        '--hidden-import=PyQt6.QtWidgets',
        '--hidden-import=PyQt6.QtCore',
        '--hidden-import=PyQt6.QtGui',
        '--hidden-import=yaml',
        '--hidden-import=pyperclip',
        
        # 排除冲突的 Qt 绑定
        '--exclude-module=PyQt5',
        '--exclude-module=PySide6',
        '--exclude-module=PySide2',
        
        # 优化
        '--optimize=2',                          # Python优化级别
    ]
    
    # 运行 PyInstaller
    subprocess.check_call([sys.executable, '-m', 'PyInstaller'] + pyinstaller_args)


def create_output():
    """创建最终输出目录"""
    print("\n创建输出目录...")
    
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    # 复制打包结果到 output
    dist_app = Path(f'dist/{APP_NAME}')
    if dist_app.exists():
        for item in dist_app.iterdir():
            dest = output_dir / item.name
            if item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)
    
    # 确保 config 和 presets 目录存在且可写
    config_dir = output_dir / 'config'
    presets_dir = output_dir / 'presets'
    images_dir = output_dir / 'images'
    
    config_dir.mkdir(exist_ok=True)
    presets_dir.mkdir(exist_ok=True)
    images_dir.mkdir(exist_ok=True)
    
    # 复制配置文件（如果不存在）
    config_src = Path('src/config/options.yaml')
    config_dst = config_dir / 'options.yaml'
    if config_src.exists() and not config_dst.exists():
        shutil.copy2(config_src, config_dst)
    
    # 复制预设文件
    presets_src = Path('src/presets')
    if presets_src.exists():
        for preset_file in presets_src.glob('*.json'):
            shutil.copy2(preset_file, presets_dir / preset_file.name)
    
    # 复制 logo
    logo_src = Path('images/logo.png')
    logo_dst = images_dir / 'logo.png'
    if logo_src.exists():
        shutil.copy2(logo_src, logo_dst)
    
    print(f"\n✅ 打包完成！输出目录: {output_dir.absolute()}")
    print("\n📁 目录结构:")
    print_tree(output_dir)


def print_tree(path: Path, prefix: str = ""):
    """打印目录树"""
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{item.name}")
        if item.is_dir():
            next_prefix = "    " if is_last else "│   "
            # 限制深度，避免打印太多内容
            if prefix.count("│") < 2:
                print_tree(item, prefix + next_prefix)


def main():
    print("=" * 50)
    print("Nano Banana 提示词生成器 - 打包工具")
    print("=" * 50)
    
    # 确保在项目根目录运行
    if not os.path.exists('src/main.py'):
        print("错误: 请在项目根目录运行此脚本")
        sys.exit(1)
    
    try:
        # 1. 清理旧构建
        clean_build_dirs()
        
        # 2. 安装 PyInstaller
        install_pyinstaller()
        
        # 3. 构建 exe
        build_exe()
        
        # 4. 创建最终输出
        create_output()
        
        # 5. 清理临时文件
        clean_temp_files()
        
        print("\n" + "=" * 50)
        print("🎉 打包成功！")
        print("=" * 50)
        print("\n使用说明:")
        print("1. 将 output 文件夹压缩为 zip")
        print(f"2. 发送给用户解压后运行 {APP_NAME}.exe")
        print("\n注意: 用户可以在 config/options.yaml 中自定义选项")
        print("      预设文件保存在 presets 目录中")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 构建失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

