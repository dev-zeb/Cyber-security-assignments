
echo "pwd"
pwd
sleep 1

echo "mkdir dir1"
mkdir dir1
sleep 1

echo "cd dir1"
cd dir1
sleep 1

echo "ls -lrt"
ls -lrt
sleep 1

echo "mkdir temp"
mkdir temp
sleep 1

echo "ls -lsr"
ls -lsr
sleep 1

echo "cd temp"
cd temp
sleep 1

echo "touch new.txt"
touch new.txt
sleep 1

echo "echo 'A Random text as input' > new.txt"
echo 'A Random text as input' > new.txt
sleep 1

echo "cat new.txt"
cat new.txt
sleep 1

echo "cp new.txt copy.txt"
cp new.txt copy.txt
sleep 1

echo "echo 'A new line appended' | cat >> copy.txt"
echo 'A new line appended' | cat >> copy.txt
sleep 1

echo "cat copy.txt"
cat copy.txt
sleep 1

echo "chmod 777 copy.txt"
chmod 777 copy.txt
sleep 1

echo "mv ./copy.txt ./renamed.txt"
mv ./copy.txt ./renamed.txt
sleep 1

echo "head -10 renamed.txt"
head -10 renamed.txt
sleep 1

echo "tail -5 new.txt"
tail -5 new.txt
sleep 1

echo "rm new.txt"
rm new.txt
sleep 1

echo "cd .."
cd ..
sleep 1

echo "ls -l"
ls -l
sleep 1

echo "rm -r temp"
rm -r temp
sleep 1

echo "ls -l"
ls -l
