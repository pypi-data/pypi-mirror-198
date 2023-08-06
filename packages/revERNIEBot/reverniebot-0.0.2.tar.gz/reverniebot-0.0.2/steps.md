# 步骤记录

## 安装Chrome

### Ubuntu 

安装依赖软件
```bash
sudo apt install udev fonts-liberation libu2f-udev libvulkan1 xdg-utils -y
```

下载Chrome安装包
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

安装Chrome
```bash
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### CentOS

## 安装ChromeDriver

### 检查Chrome版本

```bash
chromedriver -version
```

### 下载ChromeDriver

前往[此处](http://npm.taobao.org/mirrors/chromedriver/)打开与Chrome版本相同的目录，根据系统下载Driver

## 安装Python依赖

```bash
pip3 install selenium
pip3 install pyvirtualdisplay
```
