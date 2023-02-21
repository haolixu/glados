@echo off

set date_time=%date:~0,-3% %time:~0,-3%
echo %date_time% >> modify.txt
echo 写入完成！

git add modify.txt
git commit -m "脚本一键更新时间"
echo 开始push...
git push
echo push完成!

pause