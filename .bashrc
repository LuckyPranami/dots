#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias la='exa -la'
alias ll='exa -l'

PS1='[\u@\h \W]\$ '

neofetch
shopt -s autocd
alias dots='git --git-dir=/home/rahul/.dots/.git --work-tree=/home/rahul'
alias ATokenG='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'
alias vi='nvim'
