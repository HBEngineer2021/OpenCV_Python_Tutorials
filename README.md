# OpenCV_Python_Tutorials

目次
<details><summary>ここをタップすると目次が見れます👀</summary>
  
- [フィルタの種類](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AE%E7%A8%AE%E9%A1%9E)
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
  - [バンドエリミネーションフィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%90%E3%83%B3%E3%83%89%E3%82%A8%E3%83%AA%E3%83%9F%E3%83%8D%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF)
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
  ```
  
  ```
  
  - OpenCV関数 + numpy
  ```
  
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
  ```
  
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
  kernel = np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]])
  # 縦の場合
  kernel = np.array([[-1,-2,-1],
                     [0,0,0],
                     [1,2,1]])
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  
  ```
  </details>

### プリューウィットフィルタ

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
  ```
  
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
  kernel = np.array([[1,1,1]
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
  ```
  
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
  ```
  
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
  ```
  
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
  
### バンドエリミネーションフィルタ

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
