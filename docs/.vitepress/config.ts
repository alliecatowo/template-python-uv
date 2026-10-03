import { defineConfig } from "vitepress";

// GitHub Pages serves project sites under /<repo>/. Set DOCS_BASE=/ for a custom domain.
export default defineConfig({
  title: "template-python-uv",
  description: "Python package template: uv, pytest, ruff, PyPI trusted publishing, mise, lefthook, CI and a VitePress docs site.",
  base: process.env.DOCS_BASE ?? "/template-python-uv/",
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [{ text: "Guide", link: "/guide/getting-started" }],
    sidebar: [
      { text: "Guide", items: [{ text: "Getting started", link: "/guide/getting-started" }] },
    ],
    socialLinks: [{ icon: "github", link: "https://github.com/alliecatowo/template-python-uv" }],
    search: { provider: "local" },
  },
});
