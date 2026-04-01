# clash-config-convert2

一个纯前端的 Clash/Mihomo 配置生成器：读取本地 `template.yaml`，在浏览器内完成参数注入、策略组裁剪和 YAML 导出。

不依赖后端 API，不上传订阅内容；`server.py` 仅用于本地静态文件服务。

## 主要特性

- 多订阅管理：新增、删除、启用/禁用单条订阅
- 批量导入订阅：支持按行导入以下格式
	- `名称,链接,前缀`
	- `名称|链接|前缀`
	- 仅链接（自动命名）
- 高级参数注入：可配置订阅更新间隔与健康检查参数
- 本地配置注入：可将本地 provider 加入 `use` 和 `proxy-providers`
- 策略组治理：支持全选/全不选/恢复默认/搜索
- 规则联动清理：取消策略组后自动清理对应规则目标
- 扩展删除目标：支持手动补充“额外删除策略组/规则目标”
- 输出控制：支持文件名自定义、时间戳追加、预览、复制、下载

## 快速开始

1. 进入项目目录并启动本地服务（不要直接双击 HTML 打开）。
2. 浏览器访问页面。
3. 填写订阅、策略组和高级设置。
4. 点击“仅预览”或“生成并下载 YAML”。

### 启动方式

方式 1（推荐，项目内置）：

```bash
python server.py
```

访问：

```text
http://127.0.0.1:7799
```

方式 2（任意静态服务也可）：

```bash
python -m http.server 7799
```

## 页面功能说明

### 1) 多订阅管理

- 至少需要 1 个“启用”订阅才能生成
- 启用订阅必须填写 `http/https` 链接
- 同名订阅会自动去重（例如 `订阅A`、`订阅A-2`）
- “清空链接”只清空 URL，不会删除行

### 2) 策略组选择

- 未勾选的可选策略组会从 `proxy-groups` 中移除
- 关联规则项会同步从 `rules` 中移除
- 支持搜索策略组名称快速筛选

默认可选组包含：

- `YouTube`、`Twitter`、`Facebook`、`Telegram`、`TikTok`
- `Netflix`、`Disney`、`Steam`、`PayPal`
- `OpenAI`、`Github`、`Google`、`Microsoft`、`Apple`、`Binance`

### 3) 高级设置

可配置项包括：

- 输出文件名（自动补 `.yaml` 后缀）
- 是否追加时间戳
- `p: &p` 区块中的订阅更新与健康检查参数
- `过滤节点`（`&GL`）和 `openai`（`&OPENAI`）锚点值
- 本地配置注入（名称/路径/前缀）
- 额外删除策略组、额外删除规则目标

## 输入示例

批量导入文本示例：

```text
机场A,https://example.com/sub/a,[A]
机场B|https://example.com/sub/b|[B]
https://example.com/sub/c
```

## 项目结构

```text
.
├─ index.html      # 页面 UI + 全部生成逻辑
├─ template.yaml   # 基础模板（生成时会替换关键区块）
├─ server.py       # 本地静态服务（ThreadingHTTPServer）
└─ README.md
```

## 工作机制

生成流程（浏览器本地执行）：

1. 通过 `fetch("template.yaml")` 读取模板
2. 替换 `p: &p` 配置块
3. 替换 `use` / `proxy-providers` 配置块
4. 替换 `&GL` 与 `&OPENAI` 过滤锚点
5. 根据勾选结果删除策略组和对应规则
6. 预览、复制或下载 YAML

## 注意事项

- 必须通过 HTTP 访问页面；`file://` 打开会触发模板读取失败
- 生成逻辑依赖模板中的关键区块格式，请勿随意改动模板结构
- 若担心订阅泄露，可先填占位链接，下载后再手工替换
- 本工具不会将订阅数据上传到远端服务

## 致谢

- clash 懒人配置项目与相关社区模板贡献者
- 原始思路来源仓库：<https://github.com/lzcmaro/clash-config-convert>
