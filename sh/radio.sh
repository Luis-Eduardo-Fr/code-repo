#!/usr/bin/env bash 
# Variável para verificar se o player "MPV" está instalado:
E_MPV=$(command -v mpv)

# Verifica se o usuário está logado como root e se o MPV está instalado:
if [[ "$UID" -eq "0" ]]; then
	printf "\033[1;31mThis script is not indeed to run as root user\033[0m\n"
	exit 1
elif [[ -z "$E_MPV" ]]; then
	printf "\e[1;31mERROR: MPV is not installed.\e[0m\n"
	exit 1
fi

# Função quando a estação digitada está cadastrada
ver_yes() {
	echo ""
	printf "\e[1;33mSearching in database\e[0m."
	sleep 1
	printf "."
	sleep 1
	printf "."
	sleep 1.5
	printf "\e[1;32mFOUND!\e[0m\n"
	sleep 3
	clear
	printf "Playing \033[1;33m$NAME\033[0m!\n"
	printf "\e[3;31mPress CTRL+C to exit\e[0m"
	mpv "$URL_RADIO" &>/dev/null
	echo ""
}

# Função quando a estação digitada não está cadastrada
ver_no() {
	echo ""
	printf "\e[1;33mSearching in database\e[0m."
	sleep 1
	printf "."
	sleep 1
	printf "."
	sleep 1.5
	printf "\e[1;31mNOT FOUND!\e[0m\n" 
	sleep 2
	clear
}


read -p "Type your radio: " radio

case $radio in
	"gaucha" | "gaúcha" | "Gaucha" | "Gaúcha" | "GAUCHA" | "GAÚCHA")
		URL_RADIO="https://liverdgaupoa.rbsdirect.com.br/primary/gaucha_rbs.sdp/chunklist_36c916a3-44bd-4777-ac8e-2805b97d216b.m3u8" 
		NAME="Gaúcha FM 93.7MHz"
		ver_yes
		;;
	"acustica" | "ACUSTICA" | "ACÚSTICA" | "acústica" | "Acústica" | "Acustica")
		URL_RADIO="https://live.virtualcast.com.br/acusticacamaqua"
		NAME="Acústica FM 97.7MHz"
		ver_yes
		;;	
	"q") 
		printf "\e[1;31mQuitting..\e[0m\n"
		sleep 0.5
		exit 0
		;;
	*)
		ver_no
		/home/lefds/Documents/code/sh/radio.sh
		;;
esac


