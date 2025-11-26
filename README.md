<p align="center">
  <img src="./images/logo.png" alt="Nano Banana Logo" width="120" />
</p>

<h1 align="center">Nano Banana 提示词生成器</h1>

<p align="center">
  <strong>结构化 AI 绘画提示词生成器</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyQt6-6.6+-green?logo=qt&logoColor=white" alt="PyQt6" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%20%7C%20Linux-lightgrey" alt="Platform" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
</p>

---

## 界面预览

![UI Preview](./images/UI_1.png)

## 快速开始

### 下载客户端使用

在[Releases]()页面下载最新客户端，目前只编译了`windows`版本，解压后双击运行。


### 通过代码运行

#### 环境要求

- Python 3.10+

#### 安装

```bash
# 克隆仓库
git clone https://github.com/your-username/nano_banana_prompt_tool.git
cd nano_banana_prompt_tool

# 安装依赖
pip install -r requirements.txt
```

#### 运行

```bash
cd src
python main.py
```

#### 打包
```bash
python .\build.py 
``` 

## 使用说明

### 基础使用

1. 启动应用后，在左侧表单区域填写各项提示词参数
2. 右侧 JSON 预览区会实时显示生成的提示词
3. 点击「复制到剪贴板」将 JSON 复制到剪贴板

### 预设管理

- **保存预设**: 点击「保存为预设」，输入名称保存当前配置
- **加载预设**: 从顶部下拉框选择已保存的预设
- **删除预设**: 点击「管理预设」→「删除预设」选择要删除的项目

### 配置下拉选项

编辑 `src/config/options.yaml` 文件可自定义各字段的下拉选项：

```yaml
风格模式:
  - "高保真二次元插画, 官方立绘风格, 赛璐璐上色"
  - "写实风格, 电影质感"

画面气质:
  - "清透, 治愈, 空灵"
  - "暗黑, 神秘, 深邃"
```

## 输出格式

生成的 JSON 提示词结构如下：

```json
{
  "风格模式": "...",
  "画面气质": "...",
  "相机": {
    "机位角度": "...",
    "构图": "...",
    "镜头特性": "...",
    "传感器画质": "..."
  },
  "场景": {
    "环境": { "地点设定": "...", "光线": "...", "天气氛围": "..." },
    "主体": {
      "整体描述": "...",
      "外形特征": { "身材": "...", "面部": "...", "头发": "...", "眼睛": "..." },
      "表情与动作": { "情绪": "...", "动作": "..." },
      "服装": { "穿着": "...", "细节": "..." },
      "配饰": "..."
    },
    "背景": { "描述": "...", "景深": "..." }
  },
  "审美控制": {
    "呈现意图": "...",
    "材质真实度": ["..."],
    "色彩风格": { "整体色调": "...", "对比度": "...", "特殊效果": "..." }
  }
}
```

## 效果

**使用提示词的时候附带了角色图**

----

* 海边中秋星野
![](./images/海边中秋星野.png)

----

* 庭院睡觉中秋星野
![](./images//庭院睡觉星野.png)

----

* 雪景下的中秋星野
![](./images/雪景下的中秋星野.png)

----





