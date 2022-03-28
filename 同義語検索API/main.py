import pandas as pd

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/synonym/")
def search_synonym(q: str = None):
    # 同義語検索
    ## 辞書読み込み
    columns = ['group_id', 'type', 'expansion', 'vocab_id',
               'relation', 'abbreviation', 'spelling', 'field',
               'heading', 'reserved1', 'reserved2']
    df = pd.read_csv('../data/synonyms.txt', skip_blank_lines=True, names=columns)
 
    ## 同義語検索
    try:
        # 1. 辞書から検索語と一致する語句を検索
        # 2. 検索語のグループ番号を検索
        target_id = df[df['heading'] == q].group_id
        # 3. 同一グループ番号の語句（＝同義語）を取得
        target_df = df[df['group_id'] == int(target_id)]
        # 4. 各レコードから同義語（見出し）のみ抽出
        synonym_df = target_df['heading']
        # 5. dfをjsonに変換
        response = synonym_df.to_json(force_ascii=False)
    except:
        # 検索失敗時の例外処理
        response = {'message': '同義語辞書に未登録の単語です.'}
 
    return response
 
 
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8888, reload=True)