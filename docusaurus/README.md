# Docusaurus HTML to single MD file

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

### Один сайт

```bash
python docusaurus_to_md.py \
  "https://rocketmq.apache.org/docs/" \
  --out-dir ./output
```

### Все из файла

```bash
python docusaurus_to_md.py \
  --targets-file seed_urls.txt \
  --out-dir ./output
```

### Полезные флаги

```bash
# сохранить исходный HTML рядом с результатом
python docusaurus_to_md.py --targets-file seed_urls.txt --out-dir ./output --save-html

# ограничить число страниц на сайт
python docusaurus_to_md.py --targets-file seed_urls.txt --out-dir ./output --max-pages 50

# использовать sitemap.xml как дополнительные seed-URL
python docusaurus_to_md.py --targets-file seed_urls.txt --out-dir ./output --use-sitemap

# поменять имя итогового файла
python docusaurus_to_md.py --targets-file seed_urls.txt --out-dir ./output --combined-filename docs_bundle.md
```
