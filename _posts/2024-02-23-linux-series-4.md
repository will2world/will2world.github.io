---
title: \[리눅스 정착기 시리즈\] 4. 리눅스 명령어에 익숙해지기 위한 치트키 - tldr
toc: true
toc_sticky: true
categories:
- linux_series
tags:
- linux
- package
---
# 리눅스 쓰는게 불편한 이유 - 명령어를 다 외워야 하는건가??
개인적으로 리눅스를 처음 접할 때 가장 불편하게 느낀 것은 CLI 환경에서 자주 사용하는 명령어들을 기억해야 하는 점이었다.
그냥 명령어를 기억하는 건 그리 어렵진 않다.
그러나 일반적으로 패키지 명령어들은 세세한 argument들까지 속속들이 기억하기는 쉽지않다.
그래서 처음에는 `--help` argument를 사용해서 manual 페이지들을 찾아보거나 구글링을 통해 기본 기능과 세부 기능들에 대해서 공부를 수시로 해야 한다.
그런데 메뉴얼을 읽는 것은 굉장한 에너지 소모를 요하는 작업이다.

터미널을 실행하고 다음의 명령어를 실행하여 우리 모두가 알고있는 `ls` 명령어의 메뉴얼 페이지를 열어보라.
```sh
ls --help
```
`ls --help`를  수행하면 다음과 같은 무지막지한 양의 메뉴얼을 접할 수 있다.
후.. 한눈에 봐도 그 양이 어마어마하다.

```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                             e.g., '--block-size=M'; see SIZE format below

  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                             change of file status information);
                             with -l: show ctime and sort by name;
                             otherwise: sort by ctime, newest first

  -C                         list entries by columns
      --color[=WHEN]         color the output WHEN; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         list all entries in directory order
  -F, --classify[=WHEN]      append indicator (one of */=>@|) to entries WHEN
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                             single-column -1, verbose -l, vertical -C

      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                             can be augmented with a --sort option, but any
                             use of --sort=none (-U) disables grouping

  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                             that points to a directory

      --hide=PATTERN         do not list implied entries matching shell PATTERN
                             (overridden by -a or -A)

      --hyperlink[=WHEN]     hyperlink file names WHEN
      --indicator-style=WORD
                             append indicator with style WORD to entry names:
                             none (default), slash (-p),
                             file-type (--file-type), classify (-F)

  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for file system usage;
                             used only with -s and per directory totals

  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                             link, show information for the file the link
                             references rather than for the link itself

  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --literal              print entry names without quoting
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                             unless program is 'ls' and output is a terminal)

  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                             literal, locale, shell, shell-always,
                             shell-escape, shell-escape-always, c, escape
                             (overrides QUOTING_STYLE environment variable)

  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                             time (-t), version (-v), extension (-X), width

      --time=WORD            select which timestamp used to display or sort;
                               access time (-u): atime, access, use;
                               metadata change time (-c): ctime, status;
                               modified time (default): mtime, modification;
                               birth time: birth, creation;
                             with -l, WORD determines which time to show;
                             with --sort=time, sort by WORD (newest first)

      --time-style=TIME_STYLE
                             time/date format with -l; see TIME_STYLE below
  -t                         sort by time, newest first; see --time
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                             with -l: show access time and sort by name;
                             otherwise: sort by access time, newest first

  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
      --zero                 end each output line with NUL, not newline
  -1                         list one file per line
      --help        display this help and exit
      --version     output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y,R,Q (powers of 1024) or KB,MB,... (powers of 1000).
Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
Also the TIME_STYLE environment variable sets the default style to use.

The WHEN argument defaults to 'always' and can also be 'auto' or 'never'.

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors(1) command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'

```
우리는 위의 이 많은 내용들 전부를 공부해야만 하는가?
물론 한번쯤은 읽어볼 수 있다.
그러나 수시로 이 메뉴얼을 꺼내봐야한다면 얼마나 지치겠는가...
(모르긴해도 이런 메뉴얼이 리눅스를 떠나게 하는데 한몫하고있지 않을까싶다.)

다행히 우리에게는 이 엄청난 메뉴얼 대신 좀 더 간단한 버전의 대안 메뉴얼을 꺼내볼 수 있는 방법이 있다.
그 방법을 본 포스팅에서 소개하고자 한다.

# tl;dr
tl;dr이라는 단어를 들어본 적이 있는가?
없는 게 없는 위키피디아에 tldr을 검색해보았다.

> TL;DR or tl;dr, short for "too long; didn't read", is internet slang indicating that a block of text has been ignored due to its length.[1] It is also used to introduce a summary of an online post or news article,[1] as well as an informal interjection.[2]
>
> Wikipedia - 'TL;DR'

한마디로 `말이 너무 많아서 안읽었다` 뭐... 그런 뜻을 가진 인터넷 은어이다.
이 인터넷 용어를 이름으로 채택한 패키지가 있다.
`tldr`!!!
우리가 찾던 그 치트키이다.

# tldr을 설치하는 방법
설치는 개인이 사용하고있는 배포판의 패키지 매니저를 통해 설치할 수 있다.
데비안 계열 리눅스 배포판에서는 다음의 명령어를 사용하여 설치하면 된다.
```sh
apt install tldr
```
다른 배포판을 사용한다면 해당 패포판의 패키지 매니저를 통해 tldr을 검색하고 설치하면 된다.

# tldr 패키지의 사용방법
사용법은 아주 간단하다.
tldr 뒤에 원하는 패키지 이름만 적어주면 앞서 나온 것 같은 엄청난 양의 메뉴얼을 전부 읽고있을 필요 없이 심플하게 요약본을 보여준다.
```sh
tldr ls
```
위 명령어를 실행하면 다음처럼 `ls`의 심플한 메뉴얼을 꺼내볼 수 있다.
```sh
  ls

  List directory contents.
  More information: https://www.gnu.org/software/coreutils/ls.

  - List files one per line:
    ls -1

  - List all files, including hidden files:
    ls -a

  - List all files, with trailing `/` added to directory names:
    ls -F

  - Long format list (permissions, ownership, size, and modification date) of all files:
    ls -la

  - Long format list with size displayed using human-readable units (KiB, MiB, GiB):
    ls -lh

  - Long format list sorted by size (descending) recursively:
    ls -lSR

  - Long format list of all files, sorted by modification date (oldest first):
    ls -ltr

  - Only list directories:
    ls -d */
```

메뉴얼의 양도 양인데 가독성이 좋도록 아주 깔끔하게 작성된 메뉴얼이지 않은가?
tldr 덕분에 우리는 어떤 명령어든 모든 argument를 기억하고 있을 필요가 없다.

자, 이제는 각자가 원하는 명령어들을 하나씩 검색해보며 실제 사용을 해볼 차례이다.
한층 리눅스 생활이 편해지는 것을 느낄 수 있을 것이다.

# 참고자료
- [Wikipedia - TL;DR](https://en.wikipedia.org/wiki/TL;DR)