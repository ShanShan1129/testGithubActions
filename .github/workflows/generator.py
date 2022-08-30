import os

#header
#ログ一覧を含まないhtml部分 cssやら説明書きやらはこれとfooterに書く
#checkbox要素のcheckedを使ってCSSに開いたり閉じたりさせている
#paddingやmarginはよくわかっていない
header="""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ログ一覧</title>
    <style>
      /* メニュー全体 */
      .menu {
        width: fit-content;
      }

      /* チェックボックスは非表示にする（内部的な Off/On の機能だけ利用する） */
      .menu input {
        display: none;
      }

      /* 開いた状態のサブメニュー */
      .menu input:checked + ul {
        display: block;
        width: fix-content;
        padding: 0rem 0rem 0rem 1rem;
      }

      /* 閉じた状態のサブメニュー */
      .menu ul {
        display: none;
        /* 下記は開閉によらず共通の設定 */
        background: #eee;
        list-style: none;
        margin: 0;
        padding: 0rem 0rem 0rem 1rem;
      }

      /* 親項目の装飾 */
      .menu label {
        display: block;
        margin: 0;
        padding: 0rem;
        background: #ddd;
        cursor: pointer;
      }

      .menu label:hover {
        background: #ccc;
      }
    </style>
  </head>
  <body>
    <h3>シャン卓のログをお前に教える</h3>
    <div class="menu">"""

#この間にul要素が入れ子になる感じで
example="""<label for="item4">項目4</label>
    <input type="checkbox" id="item4">
    <ul>
        <li>項目１－１
        <li>項目１－２
        <li>項目１－３お前に教えるooooooooooooooo
    </ul>
"""

#footer 以下略
footer="""    </div>
    <p>かっこいいCSS書けるシャンカーにこのページを託す…</p>
  </body>
</html>"""

#url
#リポジトリごとに変える
#オルガのとこなら
#https://orga-itsuka-trpg.github.io/TRPG-OCL-Rule/ログ
#になるはず
url="https://shanshan1129.github.io/testGithubActions/ログ"

#未整理なのでやらない
black_list_dir=['シャンTRPGログ2021_10_02まで']

def main():
    #ワーキングディレクトリ(ルート想定)のログフォルダの存在チェック ない場合終了
    path='.'
    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    if 'ログ' not in files_dir:
        return
    print(header)
    print(example)
    print(footer)

def generate_li():
    return


if __name__ == "__main__":
    main() 