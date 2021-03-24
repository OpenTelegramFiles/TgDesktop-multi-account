import os
if input("installare requisiti?:[Y/n]") == "Y":
    os.system("sudo apt install apt-transport-https ca-certificates curl software-properties-common")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
    os.system("sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable\"")
    os.system("sudo apt update")
    os.system("sudo apt install docker-ce")
    os.system("sudo systemctl status docker")
c = input("scaricare telegram Desktop source?(digitare \"n\" se la possedete gia' [Y/n]:")
if c == "Y":
    os.system("git clone --recursive https://github.com/telegramdesktop/tdesktop.git")
elif c == "n":
    if input("sostituire numero voip massimi? [Y/n]:") == "Y":
        if os.path.isfile("tdesktop/Telegram/SourceFiles/main/main_domain.h"):
            with open("tdesktop/Telegram/SourceFiles/main/main_domain.h", "rt") as fin:
                with open("tdesktop/Telegram/SourceFiles/main/main_domain.h", "wt") as fout:
                    voipn = input("quanti voip vuoi avere max?: ")
                    for line in fin:
                        fout.write(line.replace("static constexpr auto kMaxAccounts = 3;",
                                                "static constexpr auto kMaxAccounts = " + voipn + ";"))
    if input("usare docker e buildare la source?: [Y/n]: ") == "Y":
        os.system("docker build -t tdesktop:centos_env telegramdesktop/Telegram/build/docker/centos_env/")
        apiid = input("inserisci il tuo api id: ")
        apihash = input("inserisci api hash: ")
        if input("continuare con la build?: [Y/n]") == "Y":
            os.system("docker run --rm -it -v $PWD:/usr/src/tdesktop -e DEBUG=1 tdesktop:centos_env /usr/src/tdesktop/Telegram/build/docker/centos_env/build.sh -D TDESKTOP_API_ID="+apiid + "-D TDESKTOP_API_HASH="+apihash+" -D DESKTOP_APP_USE_PACKAGED=OFF -D DESKTOP_APP_DISABLE_CRASH_REPORTS=OFF")
    else:
        print("non trovato.")