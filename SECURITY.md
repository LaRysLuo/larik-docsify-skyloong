# GitHub Pages 发布安全

本站从 `main` 分支的 `/docs` 目录发布到 `https://docs.skyloong.cc/`。
`docs/.nojekyll` 用于直接发布 Docsify 文件，必须保留。不要依赖 Jekyll
的 `_config.yml` 排除规则，也不要将 `.htaccess` 当作 GitHub Pages 的访问控制。

## 防止系统元数据泄漏

- `.gitignore` 排除各级目录中的 `.DS_Store`、`._*`、`Thumbs.db` 等系统文件。
- 忽略规则不能移除已经被 Git 跟踪的文件，发现后必须从版本库删除。
- 提交前执行 `python3 scripts/check_metadata.py`；检查 Git 索引和本地 `docs` 目录。
  清理本地文件后重新暂存删除操作，再运行检查。
- `Check OS metadata` 工作流在 push 和 pull request 时执行同一检查。
  当前使用分支直接发布，**这个检查本身不会阻止 Pages 部署**。
  要强制执行，应为 `main` 配置分支保护，要求 PR 和 `check-metadata` 状态检查通过，
  并限制绕过；或另行迁移到检查通过后才部署的 Actions 工作流。

## 部署后验收

删除文件的变更合并到 `main` 后，等待对应的 Pages 部署成功。检查首页、侧边栏、
Markdown 文档与图片仍可访问，并确认所有已删除文件在公开站点返回 HTTP 404。
例如：

```bash
curl -sS -o /dev/null -w '%{http_code}\n' https://docs.skyloong.cc/.DS_Store
curl -sS -o /dev/null -w '%{http_code}\n' https://docs.skyloong.cc/docs_md/.DS_Store
```

也应检查中文子目录中的 `.DS_Store`、`Thumbs.db` 和 `._*` 原路径。
如仍能下载，核对 Pages 的部署提交和发布源，并检查实际使用的 CDN 缓存。

## 公开范围与历史记录

`docs` 下的文档和图片会公开发布；“内部使用”文字和前端隐藏链接不能限制下载。
内部地址、账号、凭据和截图应先确认可公开范围。此检查只覆盖系统元数据，
不替代凭据扫描或截图审查。

普通删除不会清除公开 Git 历史中的文件。若历史文件含敏感内容，需要另行评估
历史清理；若含凭据，应撤销或轮换。仅删除当前版本不能使已经公开的信息失效。
