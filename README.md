
<div align="center">
  
![opencv-logo](https://opencv.org/wp-content/uploads/2022/05/logo.png)　　　
![python-logo](https://www.python.org/static/img/python-logo.png)
![Tutorials-removebg-preview](https://user-images.githubusercontent.com/61136190/174431146-84db017b-06be-43f0-a9e1-715a17235004.png)
  
</div>



# OpenCV_Python_Tutorials

![python](https://img.shields.io/badge/python-v3.7-84a2d4.svg)
![opencv](https://img.shields.io/badge/OpenCV-v3.7-ff7964.svg)
![anaconda](https://img.shields.io/badge/Anaconda-v3.7-2f5d50.svg)
![pycharm](https://img.shields.io/badge/PyCharm-v3.7-3eb370.svg)

画像処理エンジニア検定の学習用に作成しました。

画像処理エンジニア検定の詳細は、以下のリンクを参照して下さい。

https://www.cgarts.or.jp/kentei/about/img_engineer/index.html

数式は、以下の数式エディタで作成しました。

https://www.codecogs.com/eqneditor

## 目次

<details><summary>環境構築</summary>
  
- [環境構築]()
  - [Pythonのインストール（Windowsのみ）]()
  - [IDE（統合開発環境）のインストール]()
    - [Anaconde（Spyder）]()
      - [Windows]()
      - [Mac]()
    - [PyCharm]()
      - [Windows]()
      - [Mac]()
  - [OpenCVのインストール]()
</details>

<details><summary>OpenCVの基本操作</summary>
  
- [OpenCVの基本操作]()
  - [画像の読み込み]()
  - [画像の保存]()
  - [画像の表示]()
  - []()
  
</details>

<details><summary>濃淡変換</summary>
  
- [濃淡変換]()
  - [トーンカーブ]()
  - [折れ線型トーンカーブ]()
  - [累乗型トーカーブ]()
  - [S字トーンカーブ]()
  - [ヒストグラム平坦化]()
  - [濃淡の反転]()
  - [ポスタリゼーション]()
  - [ソラリゼーション]()
  - [RGB トーンカーブ]()
  - [疑似カラー]()
  - [色相・彩度・明度]()
  - [画像間演算]()
  - [マスク処理]()
  
</details>

<details><summary>空間フィルタリング</summary>
  
- [空間フィルタリング](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AE%E7%A8%AE%E9%A1%9E) 
  - [平均化フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E5%B9%B3%E5%9D%87%E5%8C%96%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [重み付き平均化フィルタ（加重平均フィルタ）](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E9%87%8D%E3%81%BF%E4%BB%98%E3%81%8D%E5%B9%B3%E5%9D%87%E5%8C%96%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E5%8A%A0%E9%87%8D%E5%B9%B3%E5%9D%87%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ガウシアンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%AC%E3%82%A6%E3%82%B7%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [微分フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E5%BE%AE%E5%88%86%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ソーベルフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%BD%E3%83%BC%E3%83%99%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [プリューウィットフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%97%E3%83%AA%E3%83%A5%E3%83%BC%E3%82%A6%E3%82%A3%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ロバーツフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%AD%E3%83%90%E3%83%BC%E3%83%84%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [2次微分フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#2%E6%AC%A1%E5%BE%AE%E5%88%86%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ラプラシアンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%A9%E3%83%97%E3%83%A9%E3%82%B7%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ゼロ交差](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%BC%E3%83%AD%E4%BA%A4%E5%B7%AE)
  - [LoGフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#log%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [アンシャープマスキング](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%A2%E3%83%B3%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%9E%E3%82%B9%E3%82%AD%E3%83%B3%E3%82%B0)
  - [鮮鋭化フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E9%AE%AE%E9%8B%AD%E5%8C%96%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [k最近隣平均化フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#k%E6%9C%80%E8%BF%91%E9%9A%A3%E5%B9%B3%E5%9D%87%E5%8C%96%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [バイラテラルフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%90%E3%82%A4%E3%83%A9%E3%83%86%E3%83%A9%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ノンローカルミーンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%8E%E3%83%B3%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%83%9F%E3%83%BC%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [メディアンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [モザイク処理](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%A2%E3%82%B6%E3%82%A4%E3%82%AF%E5%87%A6%E7%90%86)
</details>

<details><summary>周波数フィルタリングの種類</summary>
  
- [周波数フィルタリング]()  
  - [ローパスフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%AD%E3%83%BC%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ハイパスフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%8F%E3%82%A4%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [バンドパスフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%90%E3%83%B3%E3%83%89%E3%83%91%E3%82%B9%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [バンドエリミネーションフィルタ（バンドストップフィルタ）](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%90%E3%83%B3%E3%83%89%E3%82%A8%E3%83%AA%E3%83%9F%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%90%E3%83%B3%E3%83%89%E3%82%B9%E3%83%88%E3%83%83%E3%83%97%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [高域強調フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E9%AB%98%E5%9F%9F%E5%BC%B7%E8%AA%BF%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ウィーナフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%A6%E3%82%A3%E3%83%BC%E3%83%8A%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [逆フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E9%80%86%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ジョイントバイラテラルフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%B8%E3%83%A7%E3%82%A4%E3%83%B3%E3%83%88%E3%83%90%E3%82%A4%E3%83%A9%E3%83%86%E3%83%A9%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ガイデットフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%AC%E3%82%A4%E3%83%87%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ガボールフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%AC%E3%83%9C%E3%83%BC%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ベイジアンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%99%E3%82%A4%E3%82%B8%E3%82%A2%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [カルマンフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%82%AB%E3%83%AB%E3%83%9E%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [パーティクルフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%82%AF%E3%83%AB%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
  - [ブーストラップフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%96%E3%83%BC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
</details>

<details><summary>画像の復元と生成</summary>

- [画像の復元と生成]()
  - [ぼけ・ぶれ画像の復元]()
    - []()
  
</details>

<details><summary>幾何学的変換一覧</summary>

- [幾何学的変換]()
  - [線形変換]()
    - [拡大・縮小]()
    - [回転]()
    - [鏡映変換]()
    - [せん断（スキュー）]()
    - [合成変換]()
  - [同次座標とアフィン変換・射影変換]()
    - [平行移動]()
    - [同次座標]()
    - [アフィン変換]()
    - [射影変換]()
    - [合成変換]()
  - [再標本化と補間]()
    - [再標本化]()
    - [ニアーレスネイバー]()
    - [バイリニア補間]()
    - [バイキュービック補間]()
  - [イメージモザイキング]()
  
</details>
  
<details><summary>2値画像処理一覧</summary>

- [2値画像処理]()  
  - [p-タイル法]()
  - [モード法]()
  - [判別分析法]()
  - [収縮処理]()
  - [膨張処理]()
  - [クロージング]()
  - [オープニング]()
  - [ラベリング]()
</details>
  
<details><summary>領域処理</summary>

- [領域処理]()  
  - [テクスチャ]()
  - [2次元フーリエ変換による周波数特徴量]()
  - [ガーボルフィルタ]()
  - [同時生起行列を用いた統計的特徴量]()
  - [ミーンシフト]()
  - [グラフカット]()
</details>

<details><summary>パターン・図形・特徴の検出とマッチング</summary>

- [パターン・図形・特徴の検出とマッチング]()
  - [コーナー検出]()
  - [DoG]()
  - [SIFT]()
  - [ハフ変換]()
  - [顕著性マップ]()
  
</details>

<details><summary>パターン認識</summary>

- [パターン認識]()
  - [NN法とkNN法]()
  - [kd-tree法]()
  - [アダブースト]()
  - [サポートベクターマシン]()
  - [ニューラルネットワーク]()
  - [ランダムフォレスト]()
  - [クラスタリング]()
  - [階層的クラスタリング]()
  - [k-means法]()
- [画像認識の応用]()
  - [物体検出]()  
  - [画像検索]()    
  - [人体姿勢推定]()

</details>

<details><summary>動画像処理</summary>

- [動画像処理]()
  - [背景差分法]()
  - [フレーム間差分法]()
  - [統計的背景差分法]()
  - [オプティカルフロー]()
  - [ブロックマッチング法]()
  - [勾配法]()
  - [KLTトラッカー]()
  - [ミーンシフトトラッキング]()
  - [ベイジアンフィルタ]()
  - [カット検出]()
  - [カメラモーション推定]()
  - [時空間画像処理]()
  - [動画像からの自動ストロボ画像生成]()
</details>

<details><summary>3次元復元</summary>

- [3次元復元]()
  - []()
  - []()
  - []()
  - [エピポーラ幾何]()
  - [カメラキャリブレーション]()
  - [ステレオビジョン]()
  - [空間位置の計算]()
  - [平行ステレオ]()
  - [ステレオマッチング]()
  - [アクティブステレオ]()
  - [モーション推定と3次元復元]()
  - [既知の空間点からのカメラ位置・姿勢の推定]()
  - [画像対応点からのカメラモーションと3次元位置の推定]()
  - [大量の画像を用いた復元]()

</details>

<details><summary>光学的解析とシーンの復元</summary>

- [光学的解析とシーンの復元]()
  - [光学的解析]()
  - [放射量]()
  - [放射量の定義]()
  - [放射量の基本法則]()
  - [反射]()
  - [反射の種類]()
  - [BRDFの定義と性質]()
  - [反射モデル]()
  - [反射成分の分離]()
  - [色に基づく分離]()
  - [偏光に基づく分離]()
  - [形状の復元]()
  - [位置の推定と法線の推定]()
  - [照度差ステレオ]()
  - [参照物体を用いた照度差ステレオ]()
  - [反射特性の復元]()
  - [BRDFの計測]()
  - [反射モデルパラメータの推定]()
  - [照明環境の復元]()
  - [光源の種類と表現]()
  - [光源分布の計測]()
  - [インバースライティング]()
</details>
  
<details><summary>画像処理の数学基礎</summary>

- [画像処理の数学基礎]()  
  - [フーリエ変換]()
  - [確率]()
  - []()
</details>

<details><summary>リンク</summary>

- [リンク](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials/blob/develop/README.md#%E3%83%AA%E3%83%B3%E3%82%AF)
</details>

## 環境構築

MacOSの場合は、Pythonが既にインストール済みなっていますが、
Windowsの場合は、インストールされていないのでPythonの導入作業が必要になります。

プログラムを動かす際は、Anacondaという統合開発環境の中にあるSpyderが必要になります。

### Pythonのインストール（Windowsのみ）

### IDE（統合開発環境）

#### Anaconda

#### PyCharm

## 濃淡変換

### トーンカーブ

#### 概要

### 折れ線型トーンカーブ

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | グラフ | 実行結果 |
| - | - | - |
| ![poster_pc jpg_origin](https://user-images.githubusercontent.com/61136190/174352610-f4671ac1-cf30-4c80-8099-938d49083916.jpg) | ![tone_curve_histgram1](https://user-images.githubusercontent.com/61136190/174424135-ec94b4a5-5529-4e06-b511-5201c2676d43.png) | ![poster_pc_tonecurve](https://user-images.githubusercontent.com/61136190/174352159-4e9adf9c-3c85-4229-97ae-c775e4ecf157.jpg) |

| 入力画像 | グラフ | 実行結果 |
| - | - | - |
| ![poster_pc jpg_origin](https://user-images.githubusercontent.com/61136190/174352610-f4671ac1-cf30-4c80-8099-938d49083916.jpg) | ![tone_curve_histgram2](https://user-images.githubusercontent.com/61136190/174424447-0bf3ac39-0d2a-4f35-bd74-359ea4a3c9b3.png) | ![poster_pc_tonecurve2](https://user-images.githubusercontent.com/61136190/174424386-3a4f02a7-8cb5-4ea3-9fff-894d9b44fdef.jpg) |

| 入力画像 | グラフ | 実行結果 |
| - | - | - |
| ![poster_pc jpg_origin](https://user-images.githubusercontent.com/61136190/174352610-f4671ac1-cf30-4c80-8099-938d49083916.jpg) | ![tone_curve_histgram3](https://user-images.githubusercontent.com/61136190/174425462-765e6f93-96f9-41bb-ae7a-7faacbba770e.png) | ![poster_pc_tonecurve3](https://user-images.githubusercontent.com/61136190/174425479-390a1cae-e9f5-4139-a434-8df4cc90583d.jpg) |

### 累乗型トーカーブ

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | グラフ | 実行結果（ヒストグラム付き） |
| - | - | - |
| ![poster_pc jpg_origin](https://user-images.githubusercontent.com/61136190/174352610-f4671ac1-cf30-4c80-8099-938d49083916.jpg) | ![gamma_histgram](https://user-images.githubusercontent.com/61136190/174426501-a9ef5468-423c-432a-bdf7-2c46b7f1d05e.png) | ![poster_pc_gamma](https://user-images.githubusercontent.com/61136190/174426487-8f80fc09-ba34-4699-8f21-d5f393a0393d.jpg) |
 
### S字トーンカーブ

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | グラフ | ヒストグラム | 実行結果 |
| - | - | - | - |
| ![poster_pc jpg_origin](https://user-images.githubusercontent.com/61136190/174352610-f4671ac1-cf30-4c80-8099-938d49083916.jpg) | ![s_tone_curve_graph](https://user-images.githubusercontent.com/61136190/174427045-997bff47-4f4c-459d-8856-a5d158435998.png) | ![s_tone_curve_histgram](https://user-images.githubusercontent.com/61136190/174427057-bad5c8e4-9531-49e7-8c12-ef9b92277948.png) | ![poster_p_s_tone_curve](https://user-images.githubusercontent.com/61136190/174426991-84504aef-0d26-4f32-93a5-7317255fc5e5.jpg) |

### ヒストグラム平坦化

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
| ![original](https://user-images.githubusercontent.com/61136190/174429832-0eb7224c-4c32-436a-96e2-291f734c6eed.png) | ![original2](https://user-images.githubusercontent.com/61136190/174429911-0f09873a-d45c-4799-aa04-121800c91e5b.png) |
| ![original_histgram](https://user-images.githubusercontent.com/61136190/174429903-17157d3f-9a57-4bf1-a9df-f3babeab335e.png) | ![original_ equalize-histogram](https://user-images.githubusercontent.com/61136190/174429920-1252ae42-e0d9-49ec-92e3-c2999ac14a17.png) |

### 濃淡の反転

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | グラフ | ヒストグラム | 実行結果 |
| - | - | - | - |
| ![original](https://user-images.githubusercontent.com/61136190/174429832-0eb7224c-4c32-436a-96e2-291f734c6eed.png) | ![negative-positive reversal_graph](https://user-images.githubusercontent.com/61136190/174434380-1c83a0de-f1b4-4d5a-974e-e1252e158676.png) | ![negative-positive reversal_histogram](https://user-images.githubusercontent.com/61136190/174434391-96d405b3-798b-4d44-a5bd-2882974c8c47.png) | ![original_negative-positive reversal](https://user-images.githubusercontent.com/61136190/174434163-c8ed3109-1bc6-48fd-b267-81c56cc76c1c.png) |

### ポスタリゼーション

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | グラフ | ヒストグラム |
| - | - | - |
| ![original](https://user-images.githubusercontent.com/61136190/174429832-0eb7224c-4c32-436a-96e2-291f734c6eed.png) | ![posterization_graph_original](https://user-images.githubusercontent.com/61136190/174436022-ea7fdfb8-2b2a-4ab8-8560-cac149b74e75.png) | ![posterization_histogram_original](https://user-images.githubusercontent.com/61136190/174436032-ed660ce0-d904-4635-a46b-8cd2ebf9d43c.png) |

| 実行結果（64階調） | グラフ | ヒストグラム |
| - | - | - |
| ![posterization_64](https://user-images.githubusercontent.com/61136190/174435372-a51d3730-8924-4587-ae19-97a78ff05895.png) | ![posterization_graph_64](https://user-images.githubusercontent.com/61136190/174435592-e29f3ca0-de13-4691-9514-8a5494e7f02a.png) | ![posterization_histogram_64](https://user-images.githubusercontent.com/61136190/174435609-2a7f71b6-7145-4277-a1d8-6b903d6e86bb.png) |

| 実行結果（32階調） | グラフ | ヒストグラム |
| - | - | - |
| ![posterization_32](https://user-images.githubusercontent.com/61136190/174435556-692abe5a-e472-4a84-af41-12d7f1dbaeb4.png) | ![posterization_graph_32](https://user-images.githubusercontent.com/61136190/174435621-e5e500f0-41e5-41ef-b533-891183d165ad.png) | ![posterization_histogram_32](https://user-images.githubusercontent.com/61136190/174435631-47b2701d-2ea7-487c-8724-913a340699b5.png) |

| 実行結果（16階調） | グラフ | ヒストグラム |
| - | - | - |
| ![posterization_16](https://user-images.githubusercontent.com/61136190/174435563-8793422f-2a33-49f0-9b53-d29ce669efb3.png) | ![posterization_graph_16](https://user-images.githubusercontent.com/61136190/174435642-4b4e5bea-8661-471b-af6b-fb8391287035.png) | ![posterization_histogram_16](https://user-images.githubusercontent.com/61136190/174435711-2a762e59-1b4b-4f8e-b000-72fc4c2153a4.png) |

### ソラリゼーション

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | トーンカーブ | ヒストグラム |
| - | - | - |
| ![original](https://user-images.githubusercontent.com/61136190/174429832-0eb7224c-4c32-436a-96e2-291f734c6eed.png) | ![posterization_graph_original](https://user-images.githubusercontent.com/61136190/174436022-ea7fdfb8-2b2a-4ab8-8560-cac149b74e75.png) | ![posterization_histogram_original](https://user-images.githubusercontent.com/61136190/174436032-ed660ce0-d904-4635-a46b-8cd2ebf9d43c.png) |

| 実行結果 | トーンカーブ | ヒストグラム |
| - | - | - |
| ![solarization](https://user-images.githubusercontent.com/61136190/174436814-97711bd7-2e57-42f6-8f02-89cd61a83129.png) | ![solarization_tone_curve](https://user-images.githubusercontent.com/61136190/174436899-5bd6e558-5c53-4dc7-a7c0-ca33c9b8edb8.png) | ![solarization_histogram](https://user-images.githubusercontent.com/61136190/174436881-e9c6477d-3182-4a45-88cf-5368dd34b636.png) |

### RGB トーンカーブ

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### 疑似カラー

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | トーンカーブ | 実行結果 |
| - | - | - |
| ![original](https://user-images.githubusercontent.com/61136190/174429832-0eb7224c-4c32-436a-96e2-291f734c6eed.png) | ![pseudo-color_tone-curve](https://user-images.githubusercontent.com/61136190/174438040-ed657cc8-6586-4957-997b-8d5596658c87.png) | ![pseudo-color](https://user-images.githubusercontent.com/61136190/174438054-9185d95c-f973-40f0-a780-0beb517310a9.png) |

### 色相・彩度・明度

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### 画像間演算

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### マスク処理

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

## 空間フィルタリング

### 平均化フィルタ

#### 概要

  - OpenCV関数
  ```py
  cv2.blur(img, ksize)
  ```
  
  - OpenCV関数 + numpy
  ```py
  ddepth = -1
    
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[1/9,1/9,1/9],
                       [1/9,1/9,1/9],
                       [1/9,1/9,1/9]])
    
  dst = cv2.filter2D(img, ddepth, kernel)
  ```

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |
  
  <details><summary>サンプルコード</summary>
  
  ```py
  imageName = input("画像名を入力するしてください。\n")
  
  img = cv2.imread("./img/" + imageName)
  
  a = int(input("カーネルサイズaを入力。\n"))
  b = int(input("カーネルサイズbを入力。\n"))
  ksize = (a, b)

  dst = cv2.blur(img, ksize)
  
  outputImage = input("画像名を入力するしてください。\n")
  
  cv2.imwrite("./img/" + outputImage, dst)
  ```
  </details>

### 重み付き平均化フィルタ（加重平均フィルタ）

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]], np.float32)/16
                       
  # カーネルサイズ【5 × 5】の場合
  kernel = np.array([[1,4,6,4,1],
                     [4,16,24,16,4],
                     [6,24,36,24,6],
                     [4,16,24,16,4],
                     [1,4,6,4,1]], np.float32)/256
    
  dst = cv2.filter2D(img, ddepth, kernel)
  ```

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

  <details><summary>サンプルコード</summary>
  
  ```py
  ddepth = -1
    
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]], np.float32)/16
    
  dst = cv2.filter2D(img, ddepth, kernel)
    
  outputImage = input("画像名を入力するしてください。\n")
    
  cv2.imwrite("./img/" + outputImage, dst)
  ```
  
  ```py
  ddepth = -1
  
  # カーネルサイズ【5 × 5】の場合
  kernel = np.array([[1,4,6,4,1],
                     [4,16,24,16,4],
                     [6,24,36,24,6],
                     [4,16,24,16,4],
                     [1,4,6,4,1]], np.float32)/256
    
  dst = cv2.filter2D(img, ddepth, kernel)
    
  outputImage = input("画像名を入力するしてください。\n")
    
  cv2.imwrite("./img/" + outputImage, dst)
  ```
  </details>

### ガウシアンフィルタ

  - OpenCV関数
  ```py
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  ddepth = -1
  
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], np.float32)/16
  
  dst = cv2.filter2D(img, ddepth, kernel)
  ```
#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### 微分フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  # 横方向
  kernel_x = np.array([[0, 0, 0],
                    [0, -1, 1],
                    [0, 0, 0]])
                    
  kernel_x = np.array([[0, 0, 0],
                    [-1, 1, 0],
                    [0, 0, 0]])
                    
  kernel_x = np.array([[0, 0, 0],
                     [-1/2, 0, 1/2],
                     [0, 0, 0]])
                     
  # 縦方向
  kernel_y = np.array([[0, 1, 0],
                    [0, -1, 0],
                    [0, 0, 0]])
                    
  kernel_y = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, -1, 0]])
                    
  kernel_y = np.array([[0, 1/2, 0],
                     [0, 0, 0],
                     [0, -1/2, 0]])
  ```

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ソーベルフィルタ

  - OpenCV関数
  ```py
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  # 横の場合
  kernel_x = np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]])
  # 縦の場合
  kernel_y = np.array([[-1,-2,-1],
                     [0,0,0],
                     [1,2,1]])
  ```

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### プリューウィットフィルタ

  - OpenCV関数
  ```py
  
  ```
  - OpenCV関数 + numpy
  ```py
  # 横方向
  kernel_x = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])
  # 縦方向
  kernel_y = np.array([[1,1,1],
                       [0,0,0],
                       [-1,-1,-1]])
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ロバーツフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### 2次微分フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  # 横方向
  kernel = np.array([[0,0,0],
                     [1,-2,1],
                     [0,0,0]])
  # 縦方向
  kernel = np.array([[0,1,0],
                     [0,-2,0],
                     [0,1,0]])
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ラプラシアンフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  # 4近傍
  kernel = np.array([[0,1,0],
                     [1,-4,1],
                     [0,1,0]])
  # 8近傍
  kernel = np.array([[1,1,1],
                     [1,-8,1],
                     [1,1,1]])
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ゼロ交差

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### LoGフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  kernel = np.array([[0, 0, 1, 0, 0],
                     [0, 1, 2, 1, 0],
                     [1, 2, -16, 2, 1],
                     [0, 1, 2, 1, 0],
                     [0, 0, 1, 0, 0]])
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### アンシャープマスキング

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### 鮮鋭化フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  ddepth = -1
  
  k = 9
  
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[-k/9, -k/9, -k/9],
                     [-k/9, 1 + 8/9 * k, -k/9],
                     [-k/9, -k/9, -k/9]])
  
  dst = cv2.filter2D(img, ddepth, kernel)
  ```
  
  ```py
  # 入力画像
  img = cv2.imread("./path")
  
  # 平滑化
  kernel = np.array([[1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9]])
  
  # 平均化フィルタ
  average = cv2.filter2D(img, -1, kernel)
  
  # 入力画像 - 平均化フィルタの差分画像
  diff = img - average
  
  # diffをk倍してから、入力画像を加算する（鮮鋭化フィルタ）
  k = 9
  sharpen = img + k * diff
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### k最近隣平均化フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### バイラテラルフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ノンローカルミーンフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### メディアンフィルタ

  - OpenCV関数
  ```py
  dst = cv2.medianBlur(gray, ksize=13)
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### モザイク処理

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

## 周波数フィルタリング

### ローパスフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
   # 高速フーリエ変換(2次元)
    src = np.fft.fft2(src)
    
    # 画像サイズ
    h, w = src.shape
   
    # 画像の中心座標
    cy, cx =  int(h/2), int(w/2)
    
    # フィルタのサイズ(矩形の高さと幅)
    rh, rw = int(a*cy), int(a*cx)

    # 第1象限と第3象限、第1象限と第4象限を入れ替え
    fsrc =  np.fft.fftshift(src)  

    # 入力画像と同じサイズで値0の配列を生成
    fdst = np.zeros(src.shape, dtype=complex)

    # 中心部分の値だけ代入（中心部分以外は0のまま）
    fdst[cy-rh:cy+rh, cx-rw:cx+rw] = fsrc[cy-rh:cy+rh, cx-rw:cx+rw]
    
    # 第1象限と第3象限、第1象限と第4象限を入れ替え(元に戻す)
    fdst =  np.fft.fftshift(fdst)

    # 高速逆フーリエ変換 
    dst = np.fft.ifft2(fdst)
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ハイパスフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### バンドパスフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>
  
### バンドエリミネーションフィルタ（バンドストップフィルタ）

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```py
  fn = samplerate / 2                           #ナイキスト周波数
  wp = fp / fn                                  #ナイキスト周波数で通過域端周波数を正規化
  ws = fs / fn                                  #ナイキスト周波数で阻止域端周波数を正規化
  N, Wn = signal.buttord(wp, ws, gpass, gstop)  #オーダーとバターワースの正規化周波数を計算
  b, a = signal.butter(N, Wn, "bandstop")       #フィルタ伝達関数の分子と分母を計算
  y = signal.filtfilt(b, a, x) 
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### 高域強調フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ウィーナフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### 逆フィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ジョイントバイラテラルフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ガイデットフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ガボールフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ベイジアンフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### カルマンフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### パーティクルフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### ブーストラップフィルタ

  - OpenCV関数
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

## 2画像処理処理

### p-タイル法

#### 概要

p-タイル法は、画像中の文字を占める領域の画像数が、文字の大きさと撮影条件からあらかじめ予測できる場合に、予測された画素数に応じて閾値を決める手法である。p-タイル法では、
画素数を超えたときの画素値（また、超える直前の画素数）をしきい値とする。この手法は、対象画像に対する事前の知識が必要なため、未知の画像を処理する場合には適していない。

#### 処理手順

1．入力画像にグレースケールを掛ける。

2．入力画像の面積比を求める。

3．累積和で画素値を計算する。

4．画素数を超えたときの画素値をしきい値に設定する。

#### 実行結果

|ヒストグラム（閾値：100）|
| - |
| ![Figure_p_tile](https://user-images.githubusercontent.com/61136190/173852948-f531b868-3ded-4b84-902c-6beef662e1e9.png) |

| 入力画像 | 実行結果 |
| - | - |
| ![入力画像](https://user-images.githubusercontent.com/61136190/173845134-56aa0453-2124-4c68-8ffc-deea4a798666.jpg) | ![実行結果](https://user-images.githubusercontent.com/61136190/173843088-227a0627-1eb2-4606-9c30-54fdf684e1d4.jpg) |

### モード法

#### 概要

モード法は、山と山の間の谷が2つを分離するよい手がかりと考え、その谷の底を閾値とする。しかし、この方法は、画像に十分な画素数がないとノイズによって山や谷がはっきりと現れないため、谷の底を自動かつ安定に検出することが困難になり、応用に応じて工夫する必要がある。ほとんど場合、応用ごとにノイズによる影響を軽減する経験に基づいて処理を加えることが多い。

#### 処理手順

1．入力画像にグレースケールを掛ける。

2．

3．

4．

#### 実行結果

|ヒストグラム（最小値：80, 最大値：200, 閾値：96）|
| - |
| ![Figure_mode](https://user-images.githubusercontent.com/61136190/173852702-e9dd6bd0-6787-4a26-9d3a-33018401383b.png) |

| 入力画像 | 実行結果 |
| - | - |
| ![入力画像](https://user-images.githubusercontent.com/61136190/173845134-56aa0453-2124-4c68-8ffc-deea4a798666.jpg) | ![実行結果](https://user-images.githubusercontent.com/61136190/173851132-50c61934-9f33-4443-bbbc-0f50e8683bd6.jpg) |

### 判別分析法（大津の2値化）

#### 概要

黒画素クラスに属する画素と白画素クラスに属する画素は、ある閾値tの左右で分かれて分布するが、その分布の分離度が大きくなるように閾値tを決める方法が判別分析法である。分離度は、クラス間分散とクラス内分散の比で定義される。

#### 処理手順

1．入力画像にグレースケールを掛ける。

2．

3．

4．

#### 実行結果

|ヒストグラム（閾値：176）|
| - |
| ![Figure_otsu](https://user-images.githubusercontent.com/61136190/173856209-5f4f2ade-e0c4-4306-8168-e01c2c2060ed.png) |

| 入力画像 | 実行結果 |
| - | - |
| ![入力画像](https://user-images.githubusercontent.com/61136190/173845134-56aa0453-2124-4c68-8ffc-deea4a798666.jpg) | ![実行結果](https://user-images.githubusercontent.com/61136190/173855818-03bf1849-6d31-4f63-87ab-2e3152688431.jpg) |

### 収縮処理

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### 膨張処理

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### クロージング

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### オープニング

#### 概要

#### 処理手順

1．

2．

3．

4．

#### 実行結果

| 入力画像 | 実行結果 |
| - | - |
|  |  |

## 画像の復元と生成

### ぼけ・ぶれ画像の復元

#### 概要

原画像に対して __点拡がり関数（Point Spread Function：PSF）__ を使用することで、劣化画像を作成することが可能である。

劣化画像のモデル化には、以下の2つある。

1．**焦点ぼけによる劣化に対する点拡がり関数のモデル化**

2．**カメラのぶれによる劣化に対する点拡がり関数のモデル化**

上記のモデル化により作成された劣化画像を復元する方法は、以下の2つある。

1．**逆フィルタ**

2．**ウィーナーフィルタ**

上記のフィルタを活用することで、ぼけやぶれに考慮した復元画像を作成することが可能である。

#### 点拡がり関数のモデル化とパラメータ

**焦点ぼけによる劣化に対する点拡がり関数のモデル化**

●　**概要**

点であったものが拡がりをもつようになる劣化。

この拡がりは、方向によらず一定。

拡がりが大きくなれば、劣化画像のぼけも大きくなる。

ローパスフィルタと同じ分布。

●　**数式**

![point_spread_function](https://user-images.githubusercontent.com/61136190/174818084-8d2c1e38-4a6b-4519-a91b-d667c74215b0.png)

●　**実行結果**

| 入力画像 | 実行結果 |
| - | - |
|  |  |

**カメラのぶれによる劣化に対する点拡がり関数のモデル化**

●　**概要**

カメラのぶれも、焦点ぼけと同様に、原画像の1点がある範囲に拡がっていること。

カメラの動きは任意に考えられるので、すべてのカメラのぶれを表すモデルは単純ではない。

ある方向に対して、ぶれが生じる。

●　**数式**

![point_spread_function2](https://user-images.githubusercontent.com/61136190/174837550-0dc378b1-6fd4-4b6b-a98a-708a9c589202.png)

●　**実行結果**

| 入力画像 | 実行結果 |
| - | - |
|  |  |

**逆フィルタ**

●　**概要**

劣化画像の2次元フーリエ変換を <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}G\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}G\left ( u,v \right )" /> 、原画像の2次元フーリエ変換を <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}F\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}F\left ( u,v \right )" /> 、点拡がり関数の2次元フーリエ変換を <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}H\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}H\left ( u,v \right )" /> 、逆フィルタを <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}K_{inv}\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}K_{inv}\left ( u,v \right )" /> と表す。

劣化画像の2次元フーリエ変換 <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}G\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}G\left ( u,v \right )" /> は、原画像の2次元フーリエ変換 <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}F\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}F\left ( u,v \right )" /> と 点拡がり関数の2次元フーリエ変換 <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}H\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}H\left ( u,v \right )" />の積で表すことが可能である。

劣化画像の2次元フーリエ変換 <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}G\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}G\left ( u,v \right )" /> に逆フィルタ <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}K_{inv}\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}K_{inv}\left ( u,v \right )" />を適用することで、原画像の2次元フーリエ変換 <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}F\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}F\left ( u,v \right )" /> を表すことが可能である。

逆フィルタ <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}K_{inv}\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}K_{inv}\left ( u,v \right )" />が発散し、劣化画像に含まれるノイズが増幅され、復元画像に大きなノイズが生じる。

●　**数式**

**逆フィルタ**

![inverse_filter](https://user-images.githubusercontent.com/61136190/174847435-1d20e715-bae0-4b8f-9f83-f16145b49d43.png)

**劣化画像に逆フィルタを適用**

![inverse_filter_deterioration](https://user-images.githubusercontent.com/61136190/174849181-85f2bb4b-03d6-482c-a458-d1f1fa12e6b3.png)

●　**実行結果**

| 入力画像 | 実行結果 |
| - | - |
|  |  |

**ウィーナフィルタ**

●　**概要**

ノイズの2次元フーリエ変換を<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}N\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}N\left ( u,v \right )" />、ウィーナフィルタを<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}K_{w}\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}K_{w}\left ( u,v \right )" />と表す。

逆フィルタ <img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}K_{inv}\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}K_{inv}\left ( u,v \right )" />が発散し、劣化画像に含まれるノイズが増幅され、復元画像に大きなノイズが生じる。

そこで、この影響を避けるため、<img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}H\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}H\left ( u,v \right )" />が0に近いときに発散しないフィルタを使用する必要がある。

●　**数式**

**ノイズに考慮した劣化画像の表現**

上記を考慮した劣化画像は、以下のように表すことが可能である。

![noise_fft](https://user-images.githubusercontent.com/61136190/175033726-5d2d08b0-fc8a-4b60-9d9a-8412d88320b0.png)

**ウィーナフィルタ**

復元画像と原画像の差を最小にするフィルタは、以下のように表すことが可能である。

![wiener_filter](https://user-images.githubusercontent.com/61136190/175037204-cdfa769e-bbb9-4825-a565-feb7a1bbdb7e.png)

実際には、ノイズ<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}N\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}N\left ( u,v \right )" />と原画像<img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{100}\bg{white}F\left&space;(&space;u,v&space;\right&space;)" title="https://latex.codecogs.com/png.image?\inline \large \dpi{100}\bg{white}F\left ( u,v \right )" />は未知であるため、代わりに、定数<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}\Gamma&space;" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}\Gamma " />を置き、以下のように表現することが多い。

![other_wiener_filter](https://user-images.githubusercontent.com/61136190/175038555-29ebf08c-1a7c-4af5-89d0-2d9f8e4cf904.png)

●　**実行結果**

| 入力画像 | 実行結果 |
| - | - |
|  |  |

### さまざまな画像復元・生成

#### ノイズ除去

●　**概要**

- 単純な線形フィルタ（平均化フィルタ、加重平均化フィルタ、ガウシアンフィルタ、ローパスフィルタ、平均化フィルタのフーリエ変換）だとエッジがなまってしまう。
- エッジを保存するような非線形フィルタ（k最近隣平均化フィルタ、バイラテラルフィルタ、ノンローカルミーンフィルタ、メディアンフィルタ）を使用することが多い。
- ノイズ除去の効果を比較すると、線形フィルタでは、空間方向のノイズが増幅する度にエッジが大きくなまってしまう。非線形フィルタでは、線形フィルタと同程度のノイズ除去の効果があり、エッジを保存している。
- 他にも、拘束付き最小2乗法によりノイズ除去を行う方法がある。
- 原画像を復元するための拘束付き最小2乗法のコスト関数は
- ベイズの定理により求められる事後確率を最大化するパラメータを求める方法は、 __事後確率最大化(Maximum A Posteriori：MAP)（MAP法）__ と呼ばれる。
-  __事後確率最大化法(Maximum A Posteriori)（MAP法）__ の評価関数と考えられる。
- 第一項は、 __尤度（liklihood）__ から、第二項は、 __事前確率（prior pobability）__ から、それぞれ導出される。
-  __事前確率（prior pobability）__ が隣接画素のみでモデル化されている場合、 __マルコフ確率場（Markov Random Field：MRF）__ からも導出される。
- 画像全体を事前確率でモデル化したり、拘束を表す汎関数を設計したりすることは困難である。
- そこで、 __パッチベース手法__ が幅広く利用されている。
-  __パッチベース手法__ とは、パッチと呼ばれる小領域からなるデータを生成する。
- 生成されたパッチは、それぞれノイズ除去処理される。
- 集められたパッチの統計的な性質が推定され、その推定された性質に基づき、ノイズ除去が行われる。
- ノイズ除去されたパッチを再合成する。
- 合成処理では、重複されている部分は平均化処理がなされる。

●　**数式**

●　**実行結果**

#### 画像超解像

●　**概要**

- 標本化により劣化した画像から、高周波成分を復元する処理を、 __画像超解像__ と呼ぶ。
-  __画像超解像__ では、画像の画素数を増加させるとともに、高周波成分を復元する。
-  __低解像度画像__ とは、画素数が少なく高周波成分を含まない画像のことである。
-  __高解像度画像__ とは、画素数が多く高周波成分を含む画像のことである。
-  __画像超解像__ とは、 __低解像度画像__ から __高解像度画像__ を復元する処理である。
-  __事例ベース超解像__ では、 __高解像度画像__ と __低解像度画像__ の対応関係を予め学習しておき、この対応関係に基づき、高解像度画像が復元される。
-  __複数フレーム超解像__ では、 複数の低解像度画像の位置ずれ情報を利用する。
- 位置ずれのある複数の低解像度画像間の位置合わせを行う。
- 得られた位置合わせ情報と複数の低解像度画像の画素値の情報に基づき、高解像度画像を復元する。

●　**数式**

●　**実行結果**

#### ハイダイナミックレンジ画像

●　**概要**

- ダイナミックレンジとは、観測可能な最大値と最小値の比として定義される。
- 8ビット量子化では、ダイナミックレンジが不足してしまう。
- 暗い領域が適性な明るさとなるようにカメラを設定すると、明るい領域は飽和し、また、明るい領域が適性な明るさとなるようにカメラを設定すると、暗い領域の量子化間隔が相対的に大きくなり、疑似輪郭が発生することがある。また、暗い領域では信号に対するノイズの比が大きくなり、ノイズが目立つ。
- そのため、露出設定の異なるダイナミックレンジの狭い複数の画像を用いて、ダイナミックレンジの広いハイダイナミックレンジ画像を生成する方法が知られている。
- 生成されたハイダイナミックレンジ画像は、10ビット画像やハイダイナミックレンジの画像形式で記録される。
- 多くの表示装置では、8ビット画像にしか対応していない。
- そのため、8ビットを超えるハイダイナミックレンジ画像を8ビット画像に変換するため、 __トーンマッピング__ という手法が用いられる。
- 露出設定が小さい時、明るい領域の情報は取得できるが、暗い領域の情報は黒つぶれている。
- 露出設定が大きい時、暗い領域の情報は取得できるが、明るい領域の情報は白飛びしている。
- 露出設定を変更した複数の画像から、ハイダイナミックレンジ画像を合成して、トーンマッピングすることにより、暗い領域も明るい領域も同時に観察できる。

●　**数式**

●　**実行結果**

#### ガイド画像を利用した画像処理

●　**概要**

- 入力画像の他にガイド画像を使用した手法がある。
- フラッシュなしの画像のノイズを除去するために、フラッシュありの画像がガイド画像として利用される。
- このような手法に、 __ジョイントバイラテラルフィルタ（joint bilateral filter）__ や、 __ガイデットフィルタ（guided filter）__ がある。

●　**数式**

__ジョイントバイラテラルフィルタ（joint bilateral filter）__ は、バイラテラルフィルタの画素値方向の重みを計算する際に、入力画像の画素値ではなく、ガイド画像の画素値を利用して計算する手法であり、以下の式で表される。

●　**実行結果**

#### ライトフィールド撮影

#### コンピュテーショナルフォトグラフィ

## 動画像処理

### 背景差分法

#### 概要

1．移動物体が移った画像から背景画像を差分する。

2．絶対値を取ったあと、差分画像の2値画像を生成する。

3．差分画像の2値画像から移動物体を取り出し、移動物体画像を生成する。

### フレーム間差分法

#### 概要

1．時間 <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}" /> の画像から時間 <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}&plus;1" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}+1" /> の画像を差分する。

2．__1__ で生成された差分画像は、絶対値を取ったあと、差分画像の2値画像を生成する。

3．時間 <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}&plus;1" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}+1" /> の画像から時間 <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}&plus;2" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}+2" />の画像を差分する。

4．__2__ で生成された差分画像は、絶対値を取ったあと、差分画像の2値画像を生成する。

5．__2__ と __4__ の論理積処理を行い、共通領域取り出すことで、時間 <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}&plus;1" title="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}t_{0}+1" /> の画像における移動物体の領域を得る。

### 統計的背景差分法

#### 概要

### オプティカルフロー

#### 概要

__オプティカルフロー__ は、異なる時間に撮影された2枚の画像間での対象の移動量をベクトルデータとして表現したもの。

### ブロックマッチング法

#### 概要

__ブロックマッチング法__ は、テンプレートマッチングを用いてオプティカルフローを求める方法である。

### 勾配法

#### 概要

__勾配法__ は、連続する2枚の画像での対象物の移動量が微小であることを前提にオプティカルフローを求める方法である。

### KLTトラッカー

#### 概要



### ミーンシフトトラッキング

#### 概要



### ベイジアンフィルタ

#### 概要



### カット検出

#### 概要



### カメラモーション推定

#### 概要

### 時空間画像処理

#### 概要

### 動画像からの自動ストロボ画像生成

#### 概要

## 3次元復元
  
### 画像と空間の幾何学的関係

#### 概要

### 透視投影モデルに基づく幾何学的関係の記述

#### 概要

### 同次座標を用いた記述

#### 概要

### エピポーラ幾何

#### 概要

### カメラキャリブレーション

#### 概要

### ステレオビジョン

#### 概要

### 空間位置の計算

#### 概要

### 平行ステレオ

#### 概要

### ステレオマッチング

#### 概要

### アクティブステレオ

#### 概要

### モーション推定と3次元復元

#### 概要

### 既知の空間点からのカメラ位置・姿勢の推定

#### 概要

### 画像対応点からのカメラモーションと3次元位置の推定

#### 概要

### 大量の画像を用いた復元

#### 概要

## 光学的解析とシーンの復元

### 光学的解析

#### 概要

### 放射量

#### 概要

### 放射量の定義

#### 概要

### 放射量の基本法則

#### 概要

### 反射

#### 概要

### 反射の種類

#### 概要

### BRDFの定義と性質

#### 概要

### 反射モデル

#### 概要

### 反射成分の分離

#### 概要

### 色に基づく分離

#### 概要

### 偏光に基づく分離

#### 概要

### 形状の復元

#### 概要

### 位置の推定と法線の推定

#### 概要

### 照度差ステレオ

#### 概要

### 参照物体を用いた照度差ステレオ

#### 概要

### 反射特性の復元

#### 概要

### RDFの計測

#### 概要

### 反射モデルパラメータの推定

#### 概要

### 照明環境の復元

#### 概要

### 光源の種類と表現

#### 概要

### 光源分布の計測

#### 概要

### インバースライティング

#### 概要

## リンク
- [OpenCVを使った画像処理](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc)
- [ディジタル画像処理[改訂第二版]](https://www.amazon.co.jp/%E3%83%87%E3%82%A3%E3%82%B8%E3%82%BF%E3%83%AB%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86-%E6%94%B9%E8%A8%82%E7%AC%AC%E4%BA%8C%E7%89%88-%E3%83%87%E3%82%A3%E3%82%B8%E3%82%BF%E3%83%AB%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%E7%B7%A8%E9%9B%86%E5%A7%94%E5%93%A1%E4%BC%9A/dp/490347464X/ref=pd_bxgy_img_sccl_1/356-9064990-2117365?pd_rd_w=dD6jK&content-id=amzn1.sym.918446e7-72f4-48c7-a672-af3b6ace2b19&pf_rd_p=918446e7-72f4-48c7-a672-af3b6ace2b19&pf_rd_r=2WM90KY8AW2P6GR3FZ8B&pd_rd_wg=lQuBK&pd_rd_r=cbe5acb2-b8f8-42a6-85f7-10d1b366d839&pd_rd_i=490347464X&psc=1)
- [画像処理エンジニア検定 エキスパート・ベーシック公式問題集[改訂第四版]](https://www.amazon.co.jp/%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E6%A4%9C%E5%AE%9A-%E3%82%A8%E3%82%AD%E3%82%B9%E3%83%91%E3%83%BC%E3%83%88%E3%83%BB%E3%83%99%E3%83%BC%E3%82%B7%E3%83%83%E3%82%AF%E5%85%AC%E5%BC%8F%E5%95%8F%E9%A1%8C%E9%9B%86-%E6%94%B9%E8%A8%82%E7%AC%AC%E5%9B%9B%E7%89%88-%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E6%A4%9C%E5%AE%9A%E5%95%8F%E9%A1%8C%E9%9B%86%E7%B7%A8%E9%9B%86%E5%A7%94%E5%93%A1%E4%BC%9A/dp/4903474658)
- [Python/OpenCV】空間フィルタリングで平滑化・輪郭検出](https://algorithm.joho.info/programming/python/opencv-spatial-filter/)
- [Pythonによる画像処理100本ノック#9 ガウシアンフィルタ](https://qiita.com/muro5866/items/f55ec1eaccdda462bde6)
- [画像処理フィルタ一覧、比較 ](https://imagingsolution.net/imaging/filter-algorithm/)
- [画像フィルタ～より容易な欠陥検出のために（前編）](https://www.visco-tech.com/newspaper/column/detail19/)
- [デジタル画像処理（空間フィルタリング）](https://qiita.com/deneimonmaru/items/4b68220f0b7ed8e3f320)
- [前処理フィルタについて](https://www.keyence.co.jp/ss/products/vision/visionbasics/basic/soft/filter.jsp)
- [【図解】画像処理の6つの種類をご紹介。画像処理メーカー7社厳選](https://jss1.jp/column/column_78/#i-9)
- [画像認識の技術ブログ | マクセルフロンティア株式会社](https://www.frontier.maxell.co.jp/blog/index.html)
- [パッシブフィルタ ガイド周波数フィルタの基礎知識](https://jp.rs-online.com/web/generalDisplay.html?id=ideas-and-advice/passive-filters-guide)
- [Pythonで画像をフーリエ変換してフィルタをかけてみた](http://radiology-technologist.info/post-1594)
- [python+opencvで画像処理の勉強4 周波数領域におけるフィルタリング](https://qiita.com/tanaka_benkyo/items/bfa35e7f08faa7b7a985)
- [ディジタル画像処理~pythonによる空間フィルタリングpart2~](https://lp-tech.net/articles/VG30d)
- [pythonで一から画像処理 (5)フーリエ変換](https://qiita.com/fugunoko/items/41c33ca163c7bb52d283)
- [PythonのSciPyでバンドストップフィルタをかける!](https://watlab-blog.com/2019/05/01/scipy-bandstop/)
- [What parameters can a fourier transformation have? / How to process the shifted result?](https://stackoverflow.com/questions/34841808/what-parameters-can-a-fourier-transformation-have-how-to-process-the-shifted)
- [2値化処理 – blog - 村上真研究室](http://makotomurakami.com/blog/2020/08/06/6534/)
- [python+opencvで画像処理の勉強2 画素ごとの濃淡変換](https://qiita.com/tanaka_benkyo/items/11a9b99b4703516711e3)
- [matplotlib – 画像やヒートマップを表示する imshow の使い方](https://pystyle.info/matplotlib-imshow/)
