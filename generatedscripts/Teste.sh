#!/bin/bash

# Este script tem como objetivo atualizar o sistema para mitigar possíveis vulnerabilidades no kernel Linux.
# Ele executa um update e upgrade do sistema, seguido de uma reinicialização.

# Atualiza o índice de pacotes.
apt-get update -y

# Realiza o upgrade dos pacotes instalados.
apt-get upgrade -y

# Realiza o dist-upgrade para lidar com as dependências do sistema.
apt-get dist-upgrade -y

# Remove pacotes obsoletos.
apt-get autoremove -y

# Limpa o cache do APT.
apt-get autoclean -y

# Reinicia o sistema para aplicar as atualizações do kernel.
reboot
