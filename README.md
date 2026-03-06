# html-to-md-documentation-converter

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python opennlp_to_md.py \
  --url https://opennlp.apache.org/docs/2.5.7/manual/opennlp.html \
  --output opennlp_manual.md
```

## Запуск из локального HTML

```bash
python opennlp_to_md.py \
  --html-file opennlp.html \
  --output opennlp_manual.md
```

## Полезные параметры

- `--keep-toc` — не удалять исходное HTML-оглавление перед конвертацией.
- `--no-global-toc` — не добавлять общее Markdown-оглавление.
- `--no-section-toc` — не добавлять оглавления внутри глав.
- `--timeout 60` — таймаут HTTP-запроса.
