# SKYLOONG 技术文档使用说明

> 本项目用于维护 SKYLOONG 内部的技术文档。
> 如需新增或编辑文档，请按以下步骤操作：

---

## 一、克隆仓库

仓库地址：
👉 [https://github.com/LaRysLuo/larik-docsify-skyloong.git](https://github.com/LaRysLuo/larik-docsify-skyloong.git)

使用以下命令将项目克隆至本地：

```bash
git clone https://github.com/LaRysLuo/larik-docsify-skyloong.git
```

---

## 二、添加 Markdown 文档

请将编写好的 Markdown 文件（`.md`）放入项目根目录中的 `docs_md/` 文件夹中，例如：

```
larik-docsify-skyloong/
├── docs_md/
│   └── 示例文档.md
```

---

## 三、配置文档目录

打开 `_sidebar.md` 文件，将新增文档的路径添加进去，确保其在导航栏中显示。例如：

```markdown
* 问题解决方案
  * [Gitea 内网代码仓库重启指南](/docs_md/Gitea内网代码仓库重启指南.md)
```

你可以根据分类自行调整层级结构，注意缩进与语法格式。

---

## 四、推送到主分支完成部署

完成编辑后，将修改内容推送到 `main` 分支，即可触发部署，文档将自动更新上线：

```bash
git add .
git commit -m "更新文档：添加 Gitea 重启指南"
git push origin main
```

---

如有疑问或建议，欢迎提 Issue 或联系项目维护者。

---

✅ 推荐配合 [Docsify](https://docsify.js.org) 进行本地预览和调试。

---

**SKYLOONG 内部使用文档，仅限授权人员编辑与查看。**
