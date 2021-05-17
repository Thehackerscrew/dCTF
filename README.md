# dCTF
- [dCTF](#dctf)
- [1. MISC](#1-misc)
    - [1.1 Encrypted Flag I Have](#11-encrypted-flag-i-have)
    - [1.2 Dragon](#12-dragon)
    - [1.3 Don't Let it run](#13-dont-let-it-run)
    - [1.4 Hidden Message](#14-hidden-message)
    - [1.5 Leaked spin](#15-leaked-spin)
    - [1.6 Extraterrestial Communication](#16-extraterrestial-communication)
    - [1.7 Powerpoint Programming](#17-powerpoint-programming)
    - [1.8 Show us your ID](#18-show-us-your-id)
    - [1.9 Company Leak](#19-company-leak)
- [2. Crypto](#2-crypto)
    - [2.1 Forgotten Secret](#21-forgotten-secret)
    - [2.2 Strong Password](#22-strong-password)
    - [2.3 Julius' ancient script](#23-julius-ancient-script)
    - [2.4 Just Take Your Time](#24-just-take-your-time)
    - [2.5 Scooby-doo](#25-scooby-doo)
    - [2.6 Private Encryption Mistake](#26-private-encryption-mistake)
    - [2.7 A Simple SP Box!](#27-a-simple-sp-box)
    - [2.8 This one is really basic](#28-this-one-is-really-basic)
    - [2.9 Data Recovery](#29-data-recovery)
    - [2.10 Lockpicking](#210-lockpicking)
- [3. Web](#3-web)
    - [3.1 DevOps vs SecOps](#31-devops-vs-secops)
    - [3.2 Simple Web](#32-simple-web)

# 1. MISC
#### 1.1 Encrypted Flag I Have

![encrypted_flag_i_have](./images/encrypted_flag_i_have.png)

First off we start with this. It looks like yoda-ism, lets take a look at the file.
![encrypted_flag_i_have](./images/EncryptedTheFlagIHave.png)

Indeed I was correct. It's Star Wars language called Aurebesh. We can use a decoder from [dcode.fr](https://www.dcode.fr/aurebesh-alphabet). It's missing {} letter's but we can add them to the flag ourself.
Once decoded the flag is: DCTF{MASTERCODEBREAKER}

#### 1.2 Dragon
![dragon](./images/dragon.png)

Let's check the file
![dragon_chall](./images/dragon_chall.png)

We use [Aperisolve](https://aperisolve.fr/4a8a0f4de960dcedac96b13267b1c0c7) to analyze the file and we got the flag from the blue spectrum
![dragon_chall_solve](./images/dragon_png_solve.png)

#### 1.3 Don't Let it run
![dont_let_it_run](./images/dont_let_it_run.png)

At first when opening the [PDF](./DontLetItRun/dragon.pdf) there's just a picture of the same dragon as in previous challege so I decided to run strings on the file

`strings -n7 dragon.pdf`

Right off the bat we can see there's javascript that looks like it's HEX encoded.

Let's grab that string and and run a command.

```bash
$ echo 766172205F3078346163393D5B2736363361435968594B272C273971776147474F272C276C6F67272C273150744366746D272C27313036387552596D7154272C27646374667B7064665F316E6A33637433647D272C273736383537376A6868736272272C2737313733343268417A4F4F51272C27373232353133504158436268272C2738333339383950514B697469272C27313434373836335256636E546F272C2731323533353356746B585547275D3B2866756E6374696F6E285F30783362316636622C5F3078316164386237297B766172205F30783536366565323D5F3078353334373B7768696C652821215B5D297B7472797B766172205F30783237353061353D7061727365496E74285F307835363665653228307831366529292B2D7061727365496E74285F307835363665653228307831366429292B7061727365496E74285F307835363665653228307831366329292B2D7061727365496E74285F307835363665653228307831373329292A2D7061727365496E74285F307835363665653228307831373129292B7061727365496E74285F307835363665653228307831373229292A2D7061727365496E74285F307835363665653228307831366129292B7061727365496E74285F307835363665653228307831366629292A7061727365496E74285F307835363665653228307831373529292B2D7061727365496E74285F307835363665653228307831373029293B6966285F30783237353061353D3D3D5F307831616438623729627265616B3B656C7365205F30783362316636625B2770757368275D285F30783362316636625B277368696674275D2829293B7D6361746368285F3078353736346134297B5F30783362316636625B2770757368275D285F30783362316636625B277368696674275D2829293B7D7D7D285F3078346163392C3078386439376629293B66756E6374696F6E205F30786128297B766172205F30783363366432303D5F3078353334373B636F6E736F6C655B5F3078336336643230283078313734295D285F307833633664323028307831366229293B7D76617220613D27626B706F646E746A636F7073796D6C78656977686F6E7374796B787372707A79272C623D2765787262737071717573746E7A717269756C697A70656565787771736F666D77273B5F30786228612C62293B66756E6374696F6E205F307835333437285F30783337646533352C5F3078313961633236297B5F30783337646533353D5F30783337646533352D30783136613B766172205F30783461633965613D5F3078346163395B5F30783337646533355D3B72657475726E205F30783461633965613B7D66756E6374696F6E205F307862285F30783339623365652C5F3078666165353433297B766172205F30783235393932333D5F30783339623365652B5F30786661653534333B5F30786128293B7D0A |unhex
var _0x4ac9=['663aCYhYK','9qwaGGO','log','1PtCftm','1068uRYmqT','dctf{pdf_1nj3ct3d}','768577jhhsbr','717342hAzOOQ','722513PAXCbh','833989PQKiti','1447863RVcnTo','125353VtkXUG'];(function(_0x3b1f6b,_0x1ad8b7){var _0x566ee2=_0x5347;while(!![]){try{var _0x2750a5=parseInt(_0x566ee2(0x16e))+-parseInt(_0x566ee2(0x16d))+parseInt(_0x566ee2(0x16c))+-parseInt(_0x566ee2(0x173))*-parseInt(_0x566ee2(0x171))+parseInt(_0x566ee2(0x172))*-parseInt(_0x566ee2(0x16a))+parseInt(_0x566ee2(0x16f))*parseInt(_0x566ee2(0x175))+-parseInt(_0x566ee2(0x170));if(_0x2750a5===_0x1ad8b7)break;else _0x3b1f6b['push'](_0x3b1f6b['shift']());}catch(_0x5764a4){_0x3b1f6b['push'](_0x3b1f6b['shift']());}}}(_0x4ac9,0x8d97f));function _0xa(){var _0x3c6d20=_0x5347;console[_0x3c6d20(0x174)](_0x3c6d20(0x16b));}var a='bkpodntjcopsymlxeiwhonstykxsrpzy',b='exrbspqqustnzqriulizpeeexwqsofmw';_0xb(a,b);function _0x5347(_0x37de35,_0x19ac26){_0x37de35=_0x37de35-0x16a;var _0x4ac9ea=_0x4ac9[_0x37de35];return _0x4ac9ea;}function _0xb(_0x39b3ee,_0xfae543){var _0x259923=_0x39b3ee+_0xfae543;_0xa();}
```
There we go, we go it unhexed and flag is looking right at us!

#### 1.4 Hidden Message

![hidden_message](./images/hidden_message.png)

Let's download the [file](./images/fri.png) and check it out. After zooming around the file I couldn't find anything unusual so I decided to run `zsteg -a fri.png` to check if there's anything hidden in the bits

```bash
$ zsteg -a images/fri.png
b1,rgb,lsb,xy       .. text: "dctf{sTeg0noGr4Phy_101}"
b3,g,lsb,xy         .. text: "I@4I)$Xl"
```
The very first line revealed us the flag!

#### 1.5 Leaked spin
![leaked_spin](./images/leaked_spin.png)

Let's check the hint first before even trying to figure out anything.

![leaked_spin_hint](./images/leaked_spin_hint.png)

So it's a kind of OSINT challenge, alright I'm confident I can do this. First I google [dragonsecsi github](https://www.google.com/search?q=dragonsecsi) and I go in [there](https://github.com/DragonSecSI). We can find that there's repository called `DCTF1-chall-leak-spin` so let's jump in there and check it out. There's a file called challenge.yml and it contains the flag:
```yml
name: "Leak Spin"
author: "Miha M."
category: Web

description: We have confident insider report that one of the flags was leaked online. Can you find it?
value: 100
type: standard

flags:
  - dctf{I_L1k3_L1evaAn_P0lkk4}

tags:
  - web

state: visible
  
version: "1.0"
```


#### 1.6 Extraterrestial Communication
![extraterrestial_communication](./images/extraterrestial_communication.png)

Let's check out the hint first.

![extraterrestial_communication_hint](./images/extraterrestial_communication_hint.png)

Hint provides us with enough information. The first images we're transmitted with SSTV a.k.a Slow Scan Television.

We can use [RX-SSTV](http://users.belgacom.net/hamradio/rxsstv.htm) for this.
With RX option Scottie 1 we can decode the signal into a picture. Play the mp3 file and let the RX-SSTV do it's magic.

![extraterrestial_communication_solve](./images/extraterrestial_communication_solve.png)

Flag: dctf{wHat_ev3n_1s_SSTV}

#### 1.7 Powerpoint Programming

![powerpoint](./images/powerpoint.png)

Let's open the [file](PowerPoint_Programming/chall.ppsx) in powerpoint. We see 3 slides one with keypad and submit button, one with Correct text and one with Wrong text. Let's check out the Animations tab, from here we can see that some of the key's have a little lightning symbol beside them which means they're being used in an animation.
Click on the Animation pane and a sidebar opens up with the animations. Scroll down and you can see full animation list.
Just follow the animation instructions in the sidebar and read the flag: dctf{ppt_1snt_v3ry_s3cur3_1s_1t}

#### 1.8 Show us your ID

![show_us_id](./images/show_us_your_id.png)

Let's check the hint first

![show_us_your_id](./images/show_us_your_ID_hint.png)

Let's open the file with `strings`. 

```
%PDF-1.3
1 0 obj
/Pages 2 0 R
/Type /Catalog
2 0 obj
/Type /Pages
/Kids [ 3 0 R ]
/Count 1
3 0 obj
/Type /Page
/Parent 2 0 R
/Resources <<
/XObject << /Im0 8 0 R >>
/ProcSet 6 0 R >>
/MediaBox [0 0 613 344]
/CropBox [0 0 613 344]
/Contents 4 0 R
/Thumb 11 0 R
4 0 obj
/Length 5 0 R
613 0 0 344 0 0 cm
/Im0 Do
endstream
5 0 obj
6 0 obj
[ /PDF /Text /ImageC ]
7 0 obj
8 0 obj
/Type /XObject
/Subtype /Image
/Name /Im0
/Filter [ /DCTDecode ]
/Width 613
/Height 344
/ColorSpace 10 0 R
/BitsPerComponent 8
/Length 9 0 R
.Photoshop 3.0
printOutput
PstSbool
Inteenum
printSixteenBitbool
printerNameTEXT
printProofSetupObjc
proofSetup
Bltnenum
builtinProof
        proofCMYK
printOutputOptions
Cptnbool
Clbrbool
RgsMbool
CrnCbool
CntCbool
Lblsbool
Ngtvbool
EmlDbool
Intrbool
BckgObjc
Rd  doub@o
Grn doub@o
```
A whole bunch of stuff.. that doesnt help much. The challenge name gave an idea. Let's grep the file.

```js
$ grep -a -o "id=.*" nyan.pdf
id="646374667b3362306261347d"?>
...
```

Still a whole lot of stufff but only one thing we're interested in `id="646374667b3362306261347d"`. That looks like a hex encoded string.
Lets use unhex on it.
```bash
$ echo 646374667b3362306261347d |unhex
dctf{3b0ba4}
```
We got the flag!

#### 1.9 Company Leak

![company_leak](./images/company_leak.png)

We get this [zipfile](./Company_Leak/leaked.zip) so lets unzip it `unzip leaked.zip`.
We got two new files. [README.md](Company_Leak/README.md) and [super_secret.zip](Company_Leak/super_secret.zip)

We tried using John the ripper to crack the hash with no success. We tried using [CRC32 cracker](https://github.com/kmyk/zip-crc-cracker) for it without success. Then after some googling we found about [bkcrack](https://github.com/kimci86/bkcrack) which was the correct program to get it cracked. Here's how it happened.

```bash
$ bkcrack -C super_secret.zip -c README.md -P README.zip -p README.md
bkcrack 1.2.2 - 2021-05-17
[20:00:18] Z reduction using 285 bytes of known plaintext
100.0 % (285 / 285)
[20:00:19] Attack on 27016 Z values at index 7
Keys: a33fbdc6 5b49420e 6589766e
66.9 % (18073 / 27016)
[20:00:23] Keys
a33fbdc6 5b49420e 6589766e

$ bkcrack -C super_secret.zip -k a33fbdc6 5b49420e 6589766e -U not_so_secret.zip password
bkcrack 1.2.2 - 2021-05-17
[20:04:46] Writing unlocked archive not_so_secret.zip with password "password"
100.0 % (2 / 2)
Wrote unlocked archive.

$ unzip not_so_secret.zip
Archive:  not_so_secret.zip
[not_so_secret.zip] README.md password:
replace README.md? [y]es, [n]o, [A]ll, [N]one, [r]ename: r
new name: not_so_secret_README.md
  inflating: not_so_secret_README.md
  inflating: top_secret.txt

£ cat top_secret.txt
I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

dctf{wew_lad_y0u_aCtually_d1d_it}

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called "Linux", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called "Linux" distributions are really distributions of GNU/Linux.

(text above is a joke)
```


# 2. Crypto
#### 2.1 Forgotten Secret

![dockerimage](./images/forgotten_secret.png)

Lets check the hint.

![dockerimagehint](./images/forgotten_secret_hint.png)

So we have a the [image file](Forgotten_Secret/image) which you can just unzip to reveal it's secrets inside. So lets do that.

```bash
$ 7z x image

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,36 CPUs Intel(R) Core(TM) i9-9980XE CPU @ 3.00GHz (50654),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5911040 bytes (5773 KiB)

Extracting archive: image
--
Path = image
Type = tar
Physical Size = 5911040
Headers Size = 16896
Code Page = UTF-8

Everything is Ok

Folders: 7
Files: 24
Size:       5889333
Compressed: 5911040

$ ls -la
drwxr-xr-x root root   4 KB Mon May 17 23:13:14 2021  .
drwxrwxrwx root root   4 KB Mon May 17 22:30:08 2021  ..
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  59c05f2c50d0d56f7c4cd484794139ac75ac1f21ddd9db596af10844635a04c7
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  67fe39750473214dd953190a3f78507ff653353d49af33494f493dce7431e498
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  853eaa6658b9e21b1373def07ee4f898da46a251f58e1a8a46337ba938f3755c
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  98c9cc069e93e9cae98bbe8369566eda72b487e9ca60509e89d9d7ee98071f0d
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  b15241aee72134a1eda317850258161406ae470b813c26a1a244f7645b553014
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  df6e2b0dba838bcc158171c209ae2c7b8aeec4a8638a2fa981abda520233a170
drwxr-xr-x root root   4 KB Fri May  7 10:38:26 2021  ee6ac2faa564229d89130079d3c24dcb016b6818c2a8f3901ad2a7de1fdb0faf
.rw-r--r-- root root 3.4 KB Fri May  7 10:38:26 2021  7dabd7d32d701c6380d8e9f053d83d050569b063fbcf7ebc65e69404bed867a5.json
.rw-r--r-- root root 5.6 MB Fri May 14 18:17:20 2021  image
.rw-r--r-- root root 674 B  Fri May 14 18:17:20 2021  manifest.json
.rw-r--r-- root root  99 B  Fri May 14 18:17:20 2021  repositories
```
Lets check out the json file first.

```json
{
  "architecture": "amd64",
  "config": {
    "Hostname": "",
    "Domainname": "",
    "User": "alice",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "SECRET_KEY=58703273357638792F423F4528482B4D6251655468566D597133743677397A24"
    ],
    "Cmd": [
      "cat",
      "/home/alice/cipher.bin"
    ],
    "Image": "sha256:c57f64aa4be71ead89638dd084c259dad21322dec97f20f12640c4803979ed48",
    "Volumes": null,
    "WorkingDir": "",
    "Entrypoint": null,
    "OnBuild": null,
    "Labels": null
  },
  "container": "430de829e1ba6b76d0b449dae382eb2bca97366266d2e2d896f0a033a1e7b40c",
  "container_config": {
    "Hostname": "430de829e1ba",
    "Domainname": "",
    "User": "alice",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
      "SECRET_KEY=58703273357638792F423F4528482B4D6251655468566D597133743677397A24"
    ],
    "Cmd": [
      "/bin/sh",
      "-c",
      "#(nop) ",
      "CMD [\"cat\" \"/home/alice/cipher.bin\"]"
    ],
    "Image": "sha256:c57f64aa4be71ead89638dd084c259dad21322dec97f20f12640c4803979ed48",
    "Volumes": null,
    "WorkingDir": "",
    "Entrypoint": null,
    "OnBuild": null,
    "Labels": {}
  },
  "created": "2021-05-07T07:38:26.332455966Z",
  "docker_version": "20.10.5",
  "history": [
    {
      "created": "2021-02-24T20:20:03.472860777Z",
      "created_by": "/bin/sh -c #(nop) ADD file:0dbb1cd66f708f54f7e6663eabf24095fcd53747bfb09912a118a77e737d9617 in / "
    },
    {
      "created": "2021-02-24T20:20:03.645833664Z",
      "created_by": "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]",
      "empty_layer": true
    },
    {
      "created": "2021-05-07T07:38:15.958998137Z",
      "created_by": "/bin/sh -c #(nop) COPY file:10b1d5253a9830ea19b3097c68c9d434b3f757225a404deb1c2fefb6ca5d49eb in /root/.ssh/id_rsa "
    },
    {
      "created": "2021-05-07T07:38:21.479522094Z",
      "created_by": "/bin/sh -c chmod 600 /root/.ssh/id_rsa"
    },
    {
      "created": "2021-05-07T07:38:21.722655712Z",
      "created_by": "/bin/sh -c #(nop)  ARG SECRET_KEY",
      "empty_layer": true
    },
    {
      "created": "2021-05-07T07:38:21.996777247Z",
      "created_by": "/bin/sh -c #(nop)  ENV SECRET_KEY=58703273357638792F423F4528482B4D6251655468566D597133743677397A24",
      "empty_layer": true
    },
    {
      "created": "2021-05-07T07:38:23.392625191Z",
      "created_by": "/bin/sh -c addgroup -S alice && adduser -S alice -G alice"
    },
    {
      "created": "2021-05-07T07:38:23.710811741Z",
      "created_by": "/bin/sh -c #(nop) COPY file:74c685a989b7fe9e41bbc0b8bdebfd5a7fc9a1c64ac2afbf58a482f005eac558 in /home/alice/cipher.bin "
    },
    {
      "created": "2021-05-07T07:38:24.855457313Z",
      "created_by": "/bin/sh -c chown alice:alice /home/alice/cipher.bin"
    },
    {
      "created": "2021-05-07T07:38:25.860302496Z",
      "created_by": "/bin/sh -c chmod 600 /home/alice/cipher.bin"
    },
    {
      "created": "2021-05-07T07:38:26.109756274Z",
      "created_by": "/bin/sh -c #(nop)  USER alice",
      "empty_layer": true
    },
    {
      "created": "2021-05-07T07:38:26.332455966Z",
      "created_by": "/bin/sh -c #(nop)  CMD [\"cat\" \"/home/alice/cipher.bin\"]",
      "empty_layer": true
    }
  ],
  "os": "linux",
  "rootfs": {
    "type": "layers",
    "diff_ids": [
      "sha256:33e8713114f88c8cb3f60c8a0a4aefe2500823b2fbbae05488b0185ba226caae",
      "sha256:d38e16a3fa56a15a4e64b3fb44aa2adcdc3201b1c0edb84241c769db67d8370f",
      "sha256:e60b30ada1c8521c7865482f3837f6da5ba98813e446034b6339ee91988cd824",
      "sha256:f652323cff13716b27165effc2f64084be82da5715a108e02c35ae336c2be66a",
      "sha256:a8923ad28101cdd08ed7b6f318e702b602b20808dde85f7c61808d68548da10c",
      "sha256:1d4334271f4299b0e04683c8a2658b4c6dd8a813c99b2d6eabace4070b989967",
      "sha256:84606a800cf88cf82678e669637aed8fcf95d88f15c36f99793be1e853972936"
    ]
  }
}
```
Whoahh! that's a lot of stuff, but we can see that there's `id_rsa` private key file, `SECRET_KEY` environment variable and `cipher.bin` encrypted file. So we probably need to use that `id_rsa` to decrypt that `cipher.bin` and we can assume `SECRET_KEY` is being used as a passphrase for the privatekey.
So first things first, lets find where the privatekey is.

```bash
$ tar -tvf layer.tar
drwx------ 0/0               0 2021-05-07 10:38 root/
drwxr-xr-x 0/0               0 2021-05-07 10:38 root/.ssh/
-rw------- 0/0            2635 2021-05-07 10:38 root/.ssh/id_rsa

$ tar -xvf layer.tar
root/
root/.ssh/
root/.ssh/id_rsa

$ cat root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABBge7WiWi
2R3XsbedLz7zheAAAAEAAAAAEAAAGXAAAAB3NzaC1yc2EAAAADAQABAAABgQDEGWD7vPEn
jtMhLD7I370N/FuMBtcLSX1oCpwbqwGpOmmVMMtaLQmTq29pSrKax5+jMWvEZUxR+nJ0Hc
gdyxsGPvP722WkfwMH+BOaq3hY8JQBuNqLWeq600N9erjVBk4e3JDQwKfbMTHYsZk8Qioq
omuyrlF+SMGMzH+M5xsC80qTIlucXAW8ix8id+aflGZWKuQHmcS4m04JFhCCjWmuO3ES96
R6oppvDtu1Lm/uQN/deBNMdzRrjiv/rHvN8sP+y7p2W/nfZMcArYJqGtbKlGaUWxZSBsmd
IdHWa28BS0BrtU0a44bcHuIGhNK2dswhasZSkRqYVD5DQMQrsw6fOmV0/GC8QyEK5d45Tq
EIoBVnbxYnFSJT6wdfDlMU3n+KF4nTOWL6AxhvmxAsn49cPn9IZoyCWVuICjQ6DXZQGw74
4rFsazmrT+ZRX3/012a8nqf2k1PSWFFJq+F9D7d3Tdkx2r5SHAYZFH7cg96IdcRCEZoIoE
Iziy1McKZLk9cAAAWAY+HzKDpq12FQ0QDSCXtt4XuqngE2ewe2o1KUFvcVD/nJZPnpf2Nq
ea+s3SIFJ+hM1+Y+UAQTmFuiTa69yM45ZgkPrilKkHi5+nnNr/g70oSRBIsjwptpoDgSCL
XCqBjvNWVm/I4FkekApDb2Z//ERh1xmfFvx3KDv4SQgfUP3q9PLbOziI3wGnjmqRczilS3
6RHpNlJwbsCOuFgUkU7zymeBzU4OGcQ9Ls+Oh1X3xaAUPSnOqhoIZRiVrS48d38o6Y9j7I
zyeiVKfTRJ7yCPmJf3KrB9u8j0DGlwzkep4OIGH/iQPHALFjfnkBYPEnC0gqRSS+y1/T2z
aXGV1lsE3bh0fuk8Cja2XrB/RZftmBfHFT2YsKGeVlOlfUX0DlxyY06v3Zu8cS2/1QaHu7
KMc2MfUc1WiDe6IzPM+/Pq5aS7IVztzMuIvNMCc2GPF2D3DtQnzmsVbddWa7OhQklhFrQo
OXFEe0mgwUcl78FlLo0xmuOL2mrIfqWEcJ9GjY5ZiqKxWhfdXvXAyXlPzOFRJwX3k9jV5G
0t2ZYVoFdovYL1bDxpOEqANLhxIFaYB/PbJQwiDWxNYrGyx2mbCcrMaikV1taBIjSy8qfL
MPcRBqc2BUsdB8U33q7Ydj5V2nfm+3gUCH655KoQHMq9vOqmn/MciYtNbg9fDwYB4O38uD
3iVSd3nEq4/TbNUlY1PoatM92Okkh0H/0CVirh6WIvrUu5dNnrj7ebY+QgQkPgKLyQYdNd
HHEZi9RVBRHYbYbjJ4CRCBmAB1SCSS42roANni1O4k0sVNn5J66B0bOSktR7MFNJEV9C9y
jVEPXQQD4CGDmRJZH+cnlVaJffw17ZkZZWSVeXfhnZOtus9V9gNLAE6M876AValfW6xKH9
Iu03T5ihMHXbuSzPZG8Nc6WKq2+UGxh5S7UCAixbJQYzuC6A5HVrn9dcDlDbkYpY/DY5GZ
BNrnUIJ1srWk0I10GbVUT+vrxGfa2UdEjZL8EWvsrFd0fKGClK0MYuTLwCAtrh0gerB7Rn
YUh70cCCW5GR8XG8+VBqhyKq0SjaH5ppzTdPcAAkpHheKDkhXoWbP2Spi2HXl6/W6pro8l
BoeZEAmEf2x+X4A+9Rg1Y74YkkjLNVbTfpuJRLwP0vR8ZOawispqmR7roirz6VnT7veeqo
0ai8Ae5bTpinu75vTSteTjSeoKZmZEx5GhH+nFdL0CFwXoczPRRe7X7WjbrNxNs7EkYqD0
HuI6QdWH/A46s768uqSoi0WpTU5q2eaE7U94xef4ndAMWUYeS4mVZYqiZsoJ85jgdGi56C
ctdImSVihnmgS3NPgPxO1YQvueEZgCMNCYdf314FtXWXfGXP45c3CFZPq9KHdt+sWC0hDb
+77SGlOIJOiVhguKwiw+WORRC87W7mVO1tUrK9JrPcXYMxV3Wpis6WKyYu2yWTvd2BAWRW
djHRj+bdAYBSCuRCsoGkDt3BNO4+BTo/AcdGJ3QnJMB+qoUcaeg+LvUwv4jDhmRl5Mj4UE
OphgXY+3oFbsyGrH4ArpZhp9KWbVY/kjl7juWOn14IiScVMSi+yiG5PkIaHfp9LRrGGy1e
hyOv30gu2NYb30nwTrYo2jNFY2Txq9Ga7cMxWqpuwkSMUBsRx5LHMoZq0knjC4ghhY/Wbf
OuxqRaGsGHe+J8kMOvbE7sdsLRGZgaxyWIGSiXozU0oqQWYYJcQ40jwscUHzJHli/G+U2R
cwQpIlX4u8zjJzRSc7RxVe4/YxeEbPtdJCCi0gJCqLdpY/adJwgAm7fCaB3YZndD/bJBdj
5mqRQPpED15FITyJ5LweORkItB+/KfsIHHCRtITVEH065o+aaCbIn17q3ToIExJujPVtTw
vuYZEA==
-----END OPENSSH PRIVATE KEY-----
```

Well well well, look at that. It's old format and definitely not one used encrypt the cipher since no tools can encrypt files with that format. So we must change the key's format into something more modern like PEM.
We can do it like this:

`puttygen id_rsa -O private-openssh -o dctf.pem` and we use the SECRET_KEY as password. 
After that we can use [cyberchef](https://gchq.github.io/CyberChef/#recipe=RSA_Decrypt('-----BEGIN%20RSA%20PRIVATE%20KEY-----%5CnProc-Type:%204,ENCRYPTED%5CnDEK-Info:%20DES-EDE3-CBC,66CD19504AE3782B%5Cn%5CndPwaWL2aUUMqy3yMdZWEMG8NOO91M6to9%2BZC9/4kLCc6om63B9lWW2KaeA/7ZJdu%5CnCTrUBwnolk4iw77UmzXFMQwXDbx5YrfBDjZgIUgF3m3TNOCkfGZ8VlQxQbG0tjYy%5CnHxQCHHt5bdnB4OWMLN8JWYH9X1Y7BzIguLW5b49%2BIqbK%2Bd2%2BBLLs1PHBqh0uW5t0%5CnUmM0hzR185mna%2B2/380G0L1kZCQ95r3YWfVeUMENH2bKHsQD1ywJthXjtE58Sl%2Bo%5CnuuDREsxDZMXd6WUsdstXrG0lkF5mDjMW2HYdeWs8GqBTvMsjalYBRZZ4PPigE2Tp%5CnmAANa5YG3wsPNxKX%2BTizLFCuE5fZy5PVYeOKhlsEoV1CBYGA2/K4Z/uGX78vNamL%5CnLRCRO/xcuds8Zc%2B6QlrsxjwoqEdh/inbJZqveCDYweWx4zJJMoXU/xb1CHOSQux4%5CnLFKbaRJ03%2Bg0wo2s4ZLEVnYIOHhOFYCdUcG2ABkCbqzpjLVmYeHOmpLpSSvPxUOL%5Cn6cNhreBsGW/SAhag1NTWExbefxJu7L6FDgtOlpxZ82aBo/Q8BbLWtscIDGaiYIla%5CnvuAE5eCdnlEWDPHBnww%2Bvc6SikhPhNuhj9bQliqYyIpHiU75F0GNlH1rcSpsesZt%5CnLRK9JfjCLdYLdIlWBGSX%2BixCEYlD20EIlu7PYU8moIRLShXxPyU/PF82DfuV3Tec%5Cn5a2xdDWvpPNYd/Wq%2BuhF2FytXvcA%2Bn43gHRhL6760xllonWuWp1w0TDcIcbkT5q7%5CnHr7CfGbo6bDqL4KS3TipdO/p7PsawtrNXL2b0NM3rHSqH4Emryc%2BlY4imxha2gkz%5Cna18mC8NZY6oSBjGHEZcdddnTbCWTZyORsQuqX0DmqXhAGCifs2iT%2B66sCnXFjubD%5CnH5yDUajIvnnt/BY6VEi6pndL3nOe1soFzCCTYhaey8bcVRbH6B489uofq60RbeEL%5CnVefF/n7G9oHN8zDikXFNCndCw74SCW2oYKCuD2WDrsoS2ZYe1AE/O1wvIGLfeWP0%5CnGDTon7k5GCy%2B8/GphKPPzRFR4lOUFC21CKpVswukYil2VmNkOYqJqlKeS8d9/3Di%5CnqbXebHRYY26Cke47zB/U2/BmOgvu0Zemlxc7SCTfnEKmyDiw0JS2erND38yCz0aw%5CnzjpmA7yV3PjQ57PZxY2FHVHkIbsyrb1mqDELUlFkuYfaUJgXRcrFX3k9aiMboGyI%5CnmO64k0hzKZ0cEthDxiLg1HzBxzPULj6iR%2BVZjEvPQFzZjEq8tTm9hDJJfzF%2BKnl/%5Cn8YuRR/jd7OfAX3d2WV3NOSqCvW6J7qnpukM/i1cTAfq7O3Gm5aZoK5QTt5apCkYG%5CnggjvD0PwPSy61URZOd2JMPo4HTHX5jG8wtueHiRgMxULgN1iLn4/B1Mw3Hq9oBG%2B%5Cnmx6Keu/3Kwmr3UiOZ4vHgNh7lngERoaJfnRi4ackhrw8%2BhDWzdYv5fRfXZb31Dlu%5Cn8ic/Y3NCrHVRyDWs8VtDKcW9%2BfXfbhzeORlDpfrJ4JW8ZgLqb/fLaFg7Ze8wONXJ%5CnmIMWxaCvoDa981LZHVRxC9UrgRRtQsNFgoFB3a9tpt3GdaazHqB71qZnMOgE88p6%5CnDgGOaKfivKBGzzLL0nVWwYhy/TU11HDlw2i7cL7StCMlw9bY4i/txt7cHon9dg5g%5CnHmB9TAU9Xcazfu3wm0uM/1AM%2BoJa08roUno32wAW2QYTGENO9C%2Bg4Wfvi0TxXjCo%5Cnm%2BfLW8XS/EArIcCplhuRtT4W5RfieZ5Slxffkz%2BrHq9SEBamAjyWvf8IHbquvoOF%5Cnl8Hyis9Ivu75bRwt0LUDUtGhu1n51RRIZeXiqAMRvDDBw1XDTLQkxBZWAxkw1LNp%5Cno/0siLyAUMV/dRQBi30tyl53o8lixZZhi7UOHHJAL0PT6c13doR/Y9MyT8BGS8EU%5CnOmo197lPFIc5O39elSwTYpS%2BKMdXBX0N2rg1PJEgprPncah%2B/85DmuE5VTCbb6Ap%5CnhO9OfK%2BxfBWXXZVPlR6/wgcmdfjOUHAScZoiTHCS5jAxeonAoQdA0SOck2AfLNL4%5CnlqEFtx%2BAppCbOlnHP7FMWgewPAvsd1z6d4U0gp6rWf4lnwNfr6hStbQvFNBn2CSe%5CnpeJWA4T0YpWR37aGhIKN9yxIkycoH3nWeNGxuUPY85s4Q8xax7y/LNCDzea5sFii%5CnctaUmZAzeXxKWidopKEtQpqq21R4B3n8/DmRGbOZiIubfwmllVK%2BvYnyi5/67eRd%5Cnouz/c15WaMp4pwLcGhP8CuFmGu%2BT8I7dFnI6TfUnyhkKRRKmPeKx5HihdyFXdGR2%5CnSysiddF7qV7hHsdRzeqhuCe2XV19JoGuQz14EYy5ZMQgNT7YsjmCfQ%3D%3D%5Cn-----END%20RSA%20PRIVATE%20KEY-----','58703273357638792F423F4528482B4D6251655468566D597133743677397A24','RSAES-PKCS1-V1_5','SHA-1')) to decrypt the `cipher.bin` with the new privatekey and password.

Vóila we got the flag `Do not hardcode keys inside images! But here you go dctf{k33p_y0r_k3ys_s4f3}.`


#### 2.2 Strong Password

![strong_password](./images/strong_password.png)

Let's check the hint!

![strong_hint](./images/strong_password_hint.png)

Alright so the hint tells us not to use `fcrackzip` which is probably the most used zip cracker. But good thing we know how to run John the ripper.

Lets do this!

```bash
$ zip2john strong_password.zip > strong.hash
ver 2.0 efh 9901 strong_password.zip/lorem_ipsum.txt PKZIP Encr: cmplen=5171, decmplen=17174, crc=CEFA3672

$ john --wordlist=/usr/share/wordlists/rockyou.txt strong.hash
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 512/512 AVX512BW 16x])
No password hashes left to crack (see FAQ)

$ john --show strong.hash
strong_password.zip/lorem_ipsum.txt:Bo38AkRcE600X8DbK3600:lorem_ipsum.txt:strong_password.zip:strong_password.zip

1 password hash cracked, 0 left

$ unzip strong_password.zip
Archive:  strong_password.zip
   skipping: lorem_ipsum.txt         unsupported compression method 99

$ 7z x strong_password.zip -pBo38AkRcE600X8DbK3600

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,36 CPUs Intel(R) Core(TM) i9-9980XE CPU @ 3.00GHz (50654),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5373 bytes (6 KiB)

Extracting archive: strong_password.zip
--
Path = strong_password.zip
Type = zip
Physical Size = 5373

Everything is Ok

Size:       17174
Compressed: 5373

$ grep -o dctf.* lorem_ipsum.txt
dctf{r0cKyoU_f0r_tHe_w1n} Etiam in volutpat nunc. Aliquam erat volutpat. Ut dapibus, sem at posuere sollicitudin, tellus elit faucibus ligula, ut malesuada leo erat eu sem. Nam nulla lacus, feugiat placerat porttitor eu, sodales quis quam. Duis efficitur, nisl ege
```
We got the flag: dctf{r0cKyoU_f0r_tHe_w1n}

#### 2.3 Julius' ancient script

![julius](./images/julius_secret_script.png)

We get a file with one line in it `rq7t{7vH_rFH_vI6_pHH1_qI67}`. Looks like a basic caesar shift cipher but there's numbers involved.
Because there are number we can use [this online tool](https://planetcalc.com/8572/)
Paste the line there and press calculate. Result is in ROT22 dctf{th3_d13_h4s_b33n_c4st}

#### 2.4 Just Take Your Time

![takeyourtime](./images/just_take_your_time.png)

Let's check the hint.

![takeyourtimehint](./images/just_take_your_time_hint.png)

Alrighty then, let's open up the [file](./Just_Take_Your_Time/just-take-your-time.py) and see what we're working with.

```py
#!/usr/bin python3

from flag import flag
from Crypto.Cipher import DES3
from time import time
from random import randint
from secrets import token_hex
from pytimedinput import timedInput

guess = 3
TIMEOUT = 1

a = randint(1000000000000000, 9999999999999999)
b = randint(1000000000000000, 9999999999999999)

print("Show me you are worthy and solve for x! You have one second.")
print("{} * {} = ".format(a, b))

answ, _ = timedInput("> ", timeOut = 1, forcedTimeout = True)

try:
    assert(a*b == int(answ))
except:
    print("You are not worthy!")
    exit(1)

key = str(int(time())).zfill(16).encode("utf-8")
secret = token_hex(16)
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
encrypted = cipher.encrypt(secret.encode("utf-8"))
print("You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!")
print(encrypted.hex())

start_time = time()
while(time() - start_time < TIMEOUT and guess > 0):
    delta = time() - start_time
    answ, _ = timedInput("> ", timeOut = TIMEOUT + 1 - delta, forcedTimeout = True)

    try:
        assert(secret == answ)
        break
    except:
        if answ != "":
            guess -= 1
            if (guess != 1):
                print("You are wrong. {} guesses remain.".format(guess))
            else:
                print("You are wrong. {} guess remains.".format(guess))

if (secret != answ):
    print("You have been unsuccessful in your quest for the flag.")
else:
    print("Congratulations! Here is your flag.")
    print(flag)
```
So it seems like our first stage is about supplying a product of two numbers. Numbers are between `1000000000000000 and 9999999999999999` shouldn't be too hard since we have python. So we device this:

```py
from pwn import *

p = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999)
p.recvline()
tmp = p.recvline().strip().decode()
info(tmp)
tmp = tmp.split(' ')
res = int(tmp[0])*int(tmp[2])
success(str(res))
p.sendlineafter("> ",str(res))
p.interactive()
```
And we try it out and we get this as a result:

```py
[*] Switching to interactive mode
You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!
21e96ee7d28cb08004001afafb7d7a592336b18d2c5b5b9704838d76107235fa
> You have been unsuccessful in your quest for the flag.
[*] Got EOF while reading in interactive
```

Alright time to look at the source code again. 

```py
key = str(int(time())).zfill(16).encode("utf-8")
secret = token_hex(16)
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
encrypted = cipher.encrypt(secret.encode("utf-8"))
print("You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!")
print(encrypted.hex())

start_time = time()
while(time() - start_time < TIMEOUT and guess > 0):
    delta = time() - start_time
    answ, _ = timedInput("> ", timeOut = TIMEOUT + 1 - delta, forcedTimeout = True)
```

So we're dealing with Triple DES encryption which is using current time as a key but also filling it with zero's to deal with the key requirement length. It's using CFB mode which is a type of Stream cipher and its using `b'00000000'` as IV.

We need to findout what that `secret` is and since token_hex(16) is always random we can't predict that so we have to decrypt the hash we got from the server. We can do it like this:

```py
t = int(time())
p.recvline()
encrypted = str(p.recvline().decode())
info(encrypted)
# t-1 is just my setting
# You could have done it with for loop like: for i in range(t, t+3) if you wanted to try more than one time
key = str(t-1).zfill(16).encode()
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
FUZZ = bytes.fromhex(encrypted)
decrypted = cipher.decrypt(FUZZ)
success(decrypted)
p.sendlineafter("> ", decrypted)
opt = p.recv(1024)
print(opt.decode())
```

After trying it out we get this:

```py
[*] 207aafe5730ee93c28255f9593eed8653b494ab65611cb51f7024d8942a4851b
[*] 2f1b2b8d62716603a9c9f90f0ca72501
Congratulations! Here is your flag.
dctf{1t_0n1y_t0Ok_2_d4y5...}

```


#### 2.5 Scooby-doo

![scooby-doo](./images/scooby-doo.png)

The hint that is shown here came in the last day since it had so very little solves.

![scooby-doo-hint](./images/scooby-doo_hint.png)

The [file](./Scooby-Doo/cipher.txt) contains 10000 lines which are all encrypted by what we can guess Enigma cipher.

Bruteforcing Enigma felt like a gross idea so we figured to try something else and we came up with this:

```bash
#!/bin/bash

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in {1..22}
do
s=$(cat cipher.txt | cut -b $j | tr -d '\n')
  for x in {0..25}
  do
      cc=${a:$x:1}
      if [[ $s == *"$c"* ]]
      then
          printf ''
      else
          printf ${a:$x:1}
      fi
   done
done
```
It compares every character by character by line and if it matches the position in the alphabet it prints it out.
After running the script for ~1sec we get the flag. (Didn't bother to write about the hours of mistakes on this.)

DCTF{TURINGWOULDBEPROUD}

#### 2.6 Private Encryption Mistake

![pem](./images/private_encryption_mistake.png)

Check the hint

![pemhint](./images/private_encryption_mistake_hint.png)

Alrighty then lets take a look at the actual file we got.

![blurred](./images/blurred.png)

Well this looks awefully familiar. There's a [blogpost](https://blog.cryptohack.org/twitter-secrets) by cryptohack that tells it's possible to create a fully functional privatekey from a poorly blurred one.
After reading the blogpost this was a walk-in-the-park. Let's fire up our OCR tool and extract the data from the image.

```py
import pytesseract

try:
    import Image, ImageOps, ImageEnhance, imread
except ImportError:
    from PIL import Image, ImageOps, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

decode = pytesseract.image_to_string(r'C:\\Users\\hackernrone\\Downloads\\blurred.png')
print(decode)
```
A little messy output like always with these OCR tools, we need to go through it by hand and this is what we get as a result.

```

MIIJKQIBAAKCAgEAupQ7hhy0AQR0LRMZgP/Kl6J3l2+U+wp1YyVB8oDYvslE3AXU
3igwX2LOYgG/JIHQ5UI2G/0Fu5iPPikh3JoUABGFyPwWsBLnohdBBtpvfRLprhbB
lsKwjZfLJIrRex+sSFkcT9zVs1VH4JfcJAbeBNK/aQdMqc1i4JQ1xsQny4ZH7TZe
CXBigK99+V05C+ENRS1uWi9ixgcbMWCCBHsTq0Kl5FIfPvVJVBr075bf7DdARSRU
Wx/FtKVMlWe/nGUTz/ezu2jOx69kd+hvtzX1JVkeY+AFi7Ldta2tNaH/8kitzoXK
JC+6A+LQXynmjQdH9RGsg7QygFjPvIcgwE8LHsMt62OKcIx5LMHlW4lvLK/EZMnr

ZEt6WwyEqHhPyP0CggEBAMplAvElBwRTMaT6FfWwi149Q+C1+ogaRc686CkCEs7p
zWjt4+Tg3cndxj/p2Q3Z1AzJH8h/vfZruAQHF/UFwXIAPmuzS1K0HgnNHxr355vs
AYfArpTJeyZoRttQOXvRhM+c887RWGXX278VVS5e5mh16Dn0rKpDcRnsVMahBhTg
+4XheX0zJRa3lOnoWgRLFGcJj9px4Gk7PkZnx24S2bCb7GUbisvtELkLfAvVcGIS
vvJGbeovAGpArRoaCbpnRL96N50zOWGqHeXJFljvNDvfpVAbykf+50d2VApvElQ3
/v7UHVZEfszMk3g1z+RLpgVmtltCsFvDSkDW9omfoJ0CggEBAIBfu08VPrN+B8iD
QpyO2BBUDei8fjdskpvehjWGDqzKNYDxdVcAdERtk6DSWuzpvwPNbTRm6u3v66yu
QkHn9gBlxX1sYe5P9ExqP2p+Au8hR/8s7bhVa8G53WX1Dl47QVSwbKVOWSWtQSwB
hiB9s1YqgAlhcKBWP6vFbavr3VBYY5ln/018rYvR1euDVTUVZdSMmbq3gScF4fhv
NESMd1Je7XjygbVTPJPi1PcT/SgyDRUwz0RPYIvLlA3qT9ae7s5WTp1fanv5MV6p
4LnekTQ/CVjWSorY7xdXTCMfBK1GF7WhVGG4fVSPX8QeIPKUxKkQXgKAFJrCSjj7
CLG5pPkCggEAflfmKUDTC4kfkXwoXzHxHkgialFPbszvzOmyB39q3E2pU5pFTChv
```

From that we need to extract the needed values to create the new RSA key. I won't bother explaining too much here so I'll just dump my [script](Private_Encryption_Mistake/private_encryption_mistake.py) and you can figure it out!

```py
from Crypto.Util.number import bytes_to_long, isPrime
from Crypto.PublicKey import RSA
from base64 import b64decode


# Partial private key received from image
upper_key = b"""
MIIJKQIBAAKCAgEAupQ7hhy0AQR0LRMZgP/Kl6J3l2+U+wp1YyVB8oDYvslE3AXU
3igwX2LOYgG/JIHQ5UI2G/0Fu5iPPikh3JoUABGFyPwWsBLnohdBBtpvfRLprhbB
lsKwjZfLJIrRex+sSFkcT9zVs1VH4JfcJAbeBNK/aQdMqc1i4JQ1xsQny4ZH7TZe
CXBigK99+V05C+ENRS1uWi9ixgcbMWCCBHsTq0Kl5FIfPvVJVBr075bf7DdARSRU
Wx/FtKVMlWe/nGUTz/ezu2jOx69kd+hvtzX1JVkeY+AFi7Ldta2tNaH/8kitzoXK
JC+6A+LQXynmjQdH9RGsg7QygFjPvIcgwE8LHsMt62OKcIx5LMHlW4lvLK/EZMnr
"""

lower_key = b"""
ZEt6WwyEqHhPyP0CggEBAMplAvElBwRTMaT6FfWwi149Q+C1+ogaRc686CkCEs7p
zWjt4+Tg3cndxj/p2Q3Z1AzJH8h/vfZruAQHF/UFwXIAPmuzS1K0HgnNHxr355vs
AYfArpTJeyZoRttQOXvRhM+c887RWGXX278VVS5e5mh16Dn0rKpDcRnsVMahBhTg
+4XheX0zJRa3lOnoWgRLFGcJj9px4Gk7PkZnx24S2bCb7GUbisvtELkLfAvVcGIS
vvJGbeovAGpArRoaCbpnRL96N50zOWGqHeXJFljvNDvfpVAbykf+50d2VApvElQ3
/v7UHVZEfszMk3g1z+RLpgVmtltCsFvDSkDW9omfoJ0CggEBAIBfu08VPrN+B8iD
QpyO2BBUDei8fjdskpvehjWGDqzKNYDxdVcAdERtk6DSWuzpvwPNbTRm6u3v66yu
QkHn9gBlxX1sYe5P9ExqP2p+Au8hR/8s7bhVa8G53WX1Dl47QVSwbKVOWSWtQSwB
hiB9s1YqgAlhcKBWP6vFbavr3VBYY5ln/018rYvR1euDVTUVZdSMmbq3gScF4fhv
NESMd1Je7XjygbVTPJPi1PcT/SgyDRUwz0RPYIvLlA3qT9ae7s5WTp1fanv5MV6p
4LnekTQ/CVjWSorY7xdXTCMfBK1GF7WhVGG4fVSPX8QeIPKUxKkQXgKAFJrCSjj7
CLG5pPkCggEAflfmKUDTC4kfkXwoXzHxHkgialFPbszvzOmyB39q3E2pU5pFTChv
"""

def get_values(priv_key):
    results = []
    data = hex(bytes_to_long(b64decode(priv_key)))
    results = data.replace('02820100', ',0x').replace('0282010100', ',0x').replace('0282020100', ',0x').split(',') # should be modified accordingly
    return results

#print ("[*] Upper key values:", get_values(upper_key))
#print ("\n")
#print ("[*] Lower key values:", get_values(lower_key))
#print ("\n")

#N_upper_bits = 0xba943b861cb40104742d131980ffca97a277976f94fb0a75632541f280d8bec944dc05d4de28305f62ce6201bf2481d0e542361bfd05bb988f3e2921dc9a14001185c8fc16b012e7a2174106da6f7d12e9ae16c196c2b08d97cb248ad17b1fac48591c4fdcd5b35547e097dc2406de04d2bf69074ca9cd62e09435c6c427cb8647ed365e09706280af7df95d390be10d452d6e5a2f62c6071b316082047b13ab42a5e4521f3ef549541af4ef96dfec37404524545b1fc5b4a54c9567bf9c6513cff7b3bb68cec7af6477e86fb735f525591e63e0058bb2ddb5adad35a1fff248adce85ca242fba03e2d05f29e68d0747f511ac83b4328058cfbc8720c04f0b1ec32deb638a708c792cc1e55b896f2cafc464c9eb
#p_lower_bits = 0x644b7a5b0c84a8784fc8fd
q = [0xca6502f12507045331a4fa15f5b08b5e3d43e0b5fa881a45cebce8290212cee9cd68ede3e4e0ddc9ddc63fe9d90dd9d40cc91fc87fbdf66bb8040717f505c172003e6bb34b52b41e09cd1f1af7e79bec0187c0ae94c97b266846db50397bd184cf9cf3ced15865d7dbbf15552e5ee66875e839f4acaa437119ec54c6a10614e0fb85e1797d332516b794e9e85a044b1467098fda71e0693b3e4667c76e12d9b09bec651b8acbed10b90b7c0bd5706212bef2466dea2f006a40ad1a1a09ba6744bf7a379d333961aa1de5c91658ef343bdfa5501bca47fee74776540a6f125437fefed41d56447ecccc937835cfe44ba60566b65b42b05bc34a40d6f6899fa09d]
#dp = 0x805fbb4f153eb37e07c883429c8ed810540de8bc7e376c929bde8635860eacca3580f175570074446d93a0d25aece9bf03cd6d3466eaedefebacae4241e7f60065c57d6c61ee4ff44c6a3f6a7e02ef2147ff2cedb8556bc1b9dd65f50e5e3b4154b06ca54e5925ad412c0186207db3562a80096170a0563fabc56dabebdd5058639967ff4d7cad8bd1d5eb8355351565d48c99bab7812705e1f86f34448c77525eed78f281b5533c93e2d4f713fd28320d1530cf444f608bcb940dea4fd69eeece564e9d5f6a7bf9315ea9e0b9de91343f0958d64a8ad8ef17574c231f04ad4617b5a15461b87d548f5fc41e20f294c4a9105e0280149ac24a38fb08b1b9a4f9
#dq_upper_bits = 0x7e57e62940d30b891f917c285f31f11e48226a514f6eccefcce9b2077f6adc4da9539a454c286f
e = 0x10001

def get_p():
    result = []
    dp = int(get_values(lower_key)[2], 16) # just comment this if you add the values inside script ^ like above
    for kp in range(1, e):
        p_mul = dp * e - 1
        if p_mul % kp == 0:
            p = (p_mul // kp) + 1
            if isPrime(p):
                result.append(p)
    return result

def get_n():
    n = [P * Q for P in get_p() for Q in q]
    return n


# Fixed reconstruct function which should be faster
def reconstruct_RSA2(pt, qt, nt):
    # Find all p * q == n combinations and make a dictionary
    combinations = {n: (x, y) for n in nt for x in pt for y in qt if n == x * y}

    if len(combinations) > 1:
        print("\n[*] Printing multiple keys\n\n")
    else:
        print("[*] Final key incoming..\n\n")
    # loop through hashmap where n = p*q combinations. n = n and p_and_q tuple where p and q
    for n, p_and_q in combinations.items():
        p, q = p_and_q[0], p_and_q[1]

        # last RSA calculations before reconstructing the private key
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        key = RSA.construct((n, e, d, p, q))
        pem = key.exportKey('PEM')
        print(pem.decode(), "\n\n\n")
        f = open('dctf_id_rsa', 'w')
        f.write(pem.decode())
        f.close

if __name__ == '__main__':
    reconstruct_RSA2(get_p(), q, get_n())
    print ("[*] Creating id_rsa...")
    import os; os.chmod('dctf_id_rsa', 0o600)
    print ("[*] Connecting to target server...")
    import paramiko
    hostname = 'dctf1-chall-private-encryption-mistake.westeurope.azurecontainer.io'
    port = 2222
    user = 'user'
    key = 'dctf_id_rsa'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user, key_filename=key, port=port)
    shell = ssh.invoke_shell()
    print(shell.recv(8192).decode())
    print(shell.recv(8192).decode())

```

That's a stripped down version of a script I used in MidnightSunCTF earlier this year which had the same idea of creating a new key from partial key. 

#### 2.7 A Simple SP Box!

![spbox](./images/sp_box.png)

Won't write much about this since I'm not the one in our team who managed to do this so I don't understand it that well.

This challenge is about [Substitution Permutation](https://en.wikipedia.org/wiki/Substitution%E2%80%93permutation_network). Looking at the [source code](SP_Box/sp_box.py).

Our available alphabet is `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%.'"+:;<=}{` which gets scrambled for 12 rounds `int(2 * ceil(log(len(message), 2)))` where message being the flag length which we can get by just connecting to the server.

We need to reverse that operation to get the correct characters for the flag, and after that we need to unscramble the flag so its actually readable. You can find solve [here](SP_Box/sp_box_solve.py) or scrolling down.

```py
from pwn import *
from string import ascii_letters, digits
from math import ceil, log

alp = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"

sb = {}

fl = 42
r = int(2 * ceil(log(fl, 2)))

p = remote('dctf1-chall-sp-box.westeurope.azurecontainer.io', 8888)
p.recvline()
ct = p.recvline().strip().decode()
info(ct)

for i in range(len(alp)):
    p.sendlineafter('> ', alp[i] * fl)
    p.recvline()
    sb[p.recvline().decode()[0]] = alp[i]

print(sb)

flag = ''
for c in ct:
    flag += sb[c]

info(flag)

def un_shuffle(m):
    global fl
    res = [''] * fl
    s1 = m[:fl // 2]
    s2 = m[fl // 2:]

    i = 0
    x = 0
    y = 0
    while i < fl:
        if i % 2 == 1:
            res[i] = s1[x]
            x += 1
        else:
            res[i] = s2[y]
            y += 1
        i += 1
    return ''.join(res)

for _ in range(r-1):
    flag = un_shuffle(flag)

success(flag)
p.sendlineafter('> ',flag)
opt = p.recv(1024)
print (opt.decode())
```

#### 2.8 This one is really basic

![basic](images/this_one_is_really_basic.png)

The description with "The answer to life, the universe, and everything." movie line from Hitchikers Guide to the Galaxy and the answer to that is 42. Let's check the [file](This_One_Is_Really_Basic/cipher.txt)

```bash
$ less cipher.txt
Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJHaG9UVlZ3VlZadGNFSmxSbGw1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFkR05GU214U2JHdzFWVEowVjFaWFNraGhSemxWVm14YU0xWnNXbUZrUjA1R1UyMTRVMkpIZHpGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm0xNFlVMHhXbk5YYlVaclVqQTFSMVV5TVRSVk1rcElaSHBHVjFaRmIzZFdha1poVjBaT2NtRkhhRk5sYlhoWFZtMHhORmxWTUhoWGJrNVlZbFZhY2xWcVFURlNNVlY1VFZSU1ZrMXJjRWxhU0hCSFZqRmFSbUl6WkZkaGExcG9WakJhVDJOdFJraGhSazVzWWxob1dGWnRNSGhPUm14V1RVaG9XR0pyTlZsWmJGWmhZMnhXY1ZGVVJsTk5WbFkxVkZaU1UxWnJNWEpqUld4aFUwaENTRlpxUm1GU2JVbDZXa1prYUdFeGNHOVdha0poVkRKT2RGSnJhR2hTYXpWeldXeG9iMWRHV25STlNHaFBVbTE0VjFSVmFHOVhSMHB5VGxac1dtSkdXbWhaTW5oW.............
```

Looks like base64 so we probably need to decode it 42 times with base64.

```bash
$ cat cipher.txt | base64 -d | base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d | base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d| base64 -d
dctf{Th1s_l00ks_4_lot_sm4ll3r_th4n_1t_d1d}
```


#### 2.9 Data Recovery

![datarec](images/data_recovery.png)

Lets check the hint

![datarechint](images/data_recovery_hint.png)

Alright, lets get on with it. Lets unzip the file we got. 

```bash
$ unzip recovered_data.zip
Archive:  recovered_data.zip
   creating: content/
  inflating: content/a.out
  inflating: content/accounting.xls
  inflating: content/alarm
  inflating: content/backup.db
  inflating: content/cat.webm
  inflating: content/code.dat
  inflating: content/compiled.exe
  inflating: content/config.cfg
  inflating: content/encrypted
  inflating: content/encrypted1
  inflating: content/fish.bmp
  inflating: content/flag.txt
  inflating: content/hint.txt
  inflating: content/how-to.png
  inflating: content/important.docx
  inflating: content/kernel.bin
  inflating: content/logo.svg
  inflating: content/logs.txt
  inflating: content/macosx.app
  inflating: content/main_base.db
  inflating: content/sauce
  inflating: content/secret.cpt
  inflating: content/secret_code.jpg
  inflating: content/security_route.zip
  inflating: content/source.zip
  inflating: content/statistics.csv
```

Lets run file command on all of them.

```
$ file ./*                                                                                                                  130 ⨯
./accounting.xls:     data
./alarm:              JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=0], baseline, precision 8, 639x629, components 3
./a.out:              data
./backup.db:          data
./cat.webm:           WebM
./code.dat:           GIF image data, version 89a, 446 x 526
./compiled.exe:       data
./config.cfg:         JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=0], progressive, precision 8, 1080x885, components 3
./encrypted:          data
./encrypted1:         ASCII text
./fish.bmp:           ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
./flag.txt:           PNG image data, 561 x 789, 8-bit colormap, non-interlaced
./hint.txt:           GIF image data, version 89a, 498 x 440
./how-to.png:         PNG image data, 561 x 789, 8-bit colormap, non-interlaced
./important.docx:     data
./kernel.bin:         data
./logo.svg:           ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
./logs.txt:           ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
./macosx.app:         ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
./main_base.db:       ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
./sauce:              JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 678x590, components 3
./secret_code.jpg:    ISO Media, MP4 v2 [ISO 14496-14]
./secret.cpt:         ISO Media, MP4 v2 [ISO 14496-14]
./security_route.zip: PNG image data, 128 x 128, 8-bit/color RGBA, non-interlaced
./source.zip:         ISO Media, MP4 v1 [ISO 14496-1:ch13]
./statistics.csv:     RIFF (little-endian) data, Web/P image, VP8 encoding, 640x476, Scaling: [none]x[none], YUV color, decoders should clamp
```

Look at that there's one ASCII text file. Wonder whats inside of it, lets check it.

```bash
$ head -10 encrypted1
OiFpbn5qampiamb8xzjfcvxYvjxqauGAamp4ampqHA8YEzUDBxoFGB4LBB5EHhIe9hcxBbYi/IzR
apdtoEUQI082sVmC9BN7Bj79xxizmPw2D765SvjmpmbhDtpzzrjGr5SdV7VTTUQmwxHa6as+oSNY
cv0Zk6T/NeREPhG9sOCUnaPkIY/Qq+X5g80Hn50UNuzDGDkfGLnbMJZWPPdlOQ/wTbm93MOcFIZA
1cVGtYMW1dfW+pURAQefu1VTMVe+yck7BMB19wOXC9y//bue6xWv9z8fE5vMxJey0pQ6J9RYBzFX
nJS+PcdT76FhcLVWU+mLXZvrgwIt9BmFwfkzQDmHxtfWYi1V3WeXN/M3AVuy1Dfcm8vRQ7ogkCnC
puLh1GB3NCzdd0anr7uf1/PAvCd5V9eZpyjhsT2e2IBakNMFuDo15HwFtgqbX4chylWdx9leHtW6
7ogXUTHxU5rXywAWFVc/X9eWmIgezn13jeQc6Kwdl0l86ddlq7u+ueGU2geBJfEAvfCQGzHHlZO1
NPxbhJc7FcizX7+oXTc3NJYIzYE678kT3lKOE8LmxFdXkLzmiRg/13fHE7bxWgv8nh3ZNo+rUbC4
nqWd7GS7nV442t9FHIZXtBBxlR85m6LdkoEnCdCIqNeDKwDeD971JXzReZqwyXNssbnRkstRsC2w
pwcfHSdNUtKQ+3Xw7Z6oNdYVbi+7kKyWgQWrmBPso9JbuuTrwp1snh4TW3K9Pm2FcUiZtERKBdCz
```

Looks like another base64 file. But after decoding it we get stuck. Doesn't seem like it is anything after that but it has to be this file according to the hint. Let's use our good friend [CyberChef](https://gchq.github.io/CyberChef/).

Use `encrypted1` file as input and select `from Base64`. After that we figured out to try Magic function with intensive mode, and that was fruitful, the very first result says that the file can be XOR'd into ZIP file. So lets do just that.

After converting it into a ZIP we can use CyberChefs [Unzip module](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'Hex','string':'6a'%7D,'Standard',false)Unzip('',false)) to get a look at the files inside. 

We get a very_important.txt which has a lot of text inside so we just do simple ctrl+f search and look for `dctf` and Vóila we got ourselves a flag

dctf{x0r_eNcRypt1on_brUt3foRce}

#### 2.10 Lockpicking

Didn't solve this one during CTF, challenge can be found [here](./Lockpicking/lockpicking.py) and solve can be found in [here](./Lockpicking/lockpicking_solve.py)


# 3. Web
#### 3.1 DevOps vs SecOps

![devopsvssecops](./images/devopsvssecops.png)

Let's check the hint just in case.

![devopshint](./images/devopsvssecops_hint.png)

Hint gives us information about CI/CD which can be done with github! So let's go find out more from their [github](https://github.com/DragonSecSI).
There's a repo called DCTF1-chall-devops-vs-secops, we check it out and we notice there's 2 different branches.
Main and devops. There's nothing in the main branch but maybe there's something in the devops. Changing branch and we see a new directory .github/workflows in the workflow directory there's ctfd.yml file

```yml
name: CTFD
on:
  push:
    branches: [ devops ]
  pull_request:
    branches: [ devops ]

jobs:
  build:
    runs-on: ubuntu-18.04
    container:
      image: docker.pkg.github.com/dragonsecsi/infra/ghactions:1.0
      credentials:
        username: Aleks-dotcom
        password: ${{ secrets.REGISTRY_TOKEN }}
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2
      - name: Checkout .github
        uses: actions/checkout@v2
        with:
          repository: dragonsecsi/.github
          path: ./data
      - name: ctfd upload challenge
        run: python3 data/setup.py ${{ secrets.ADMIN_TOKEN }}
```

Here we can see it uses a different repo `repository: dragonsecsi/.github` so we need to check that out as well since the flag wasn't here.

Going to `.github` repo we find setup.py file with the flag inside.

```py
import os
import re
import sys

def init():
    #change this:
    CTFD_TOKEN = sys.argv[1]
    #change this:
    CTFD_URL = "https://dctf.dragonsec.si"
    

    os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")

def file():
    for subdirs, dirs, files in os.walk(".."):
        for dirr in dirs:
            if "DCTF-chall" in dirr:
                return dirr

if __name__ == "__main__":
    init()
    print("dctf{H3ll0_fr0m_1T_guy}")
    os.system(f"ctf challenge sync challenge.yml ;ctf challenge install challenge.yml ")
```


#### 3.2 Simple Web

![simple_web](./images/simple_web.png)

Lets go to the [site](http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/). On checking the website, it just a basic website with a simple checkbox and submit button. On submitting the form and intercepting the request, you will notice it sends the following data to `/flag` route.

```html
flag=1&auth=0&Submit=Submit
```

On changing auth from `0` to `1` and sending the request, you will get the flag.
```bash
$ curl "http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/flag" --data "flag=1&auth=1&Submit=Submit"
There you go: dctf{w3b_c4n_b3_fun_r1ght?}
```

On changing auth from `0` to `1` and sending the request, you will get the flag.
