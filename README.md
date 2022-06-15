# OpenCV_Python_Tutorials

画像処理エンジニア検定の学習用に作成。

## 目次

- [インストール]()
  <details><summary>環境一覧</summary>
  
  </details>
- [2値化処理]()
  <details><summary>2値化処理一覧</summary>
  
  - [p-タイル法]()
  - [モード法]()
  - [判別分析法]()
  </details>
  
- [フィルタの種類](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AE%E7%A8%AE%E9%A1%9E)
  <details><summary>フィルタ一覧</summary>
  
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

- [幾何学的変換]()
  <details><summary>幾何学的変換一覧</summary>
  
  </details>
  
- [物体検出]()
  <details><summary>物体検出一覧</summary>
  
  </details>
  
- [機械学習]()
  <details><summary>機械学習一覧</summary>
  
  </details>
  
- [動画像処理]()
  <details><summary>動画像処理一覧</summary>
  
  </details>
  
- [パターン認識]()
  <details><summary>パターン認識一覧</summary>
  
  </details>

- [リンク](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials/blob/develop/README.md#%E3%83%AA%E3%83%B3%E3%82%AF)

## インストール

MacOSの場合は、Pythonが既にインストール済みなっていますが、
Windowsの場合は、インストールされていないのでPythonの導入作業が必要になります。

プログラムを動かす際は、Anacondaという統合開発環境の中にあるSpyderが必要になります。

### Pythonのインストール（Windowsのみ）

### IDE（統合開発環境）

## 2値化処理

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

## フィルタの種類

### 平均化フィルタ
  
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

## リンク
- [OpenCVを使った画像処理](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc)
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
