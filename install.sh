pkg install lolcat 

clear


echo "installing pakages " |lolcat

sleep 3

spinner=( Ooooo oOooo ooOoo oooOo ooooO oooOo ooOoo oOooo); 


count(){
  spin &
  pid=$!

  for i in `seq 1 10`
  do
    sleep 1;
  done

  kill $pid
}

spin(){
  while [ 1 ]
  do
    for i in ${spinner[@]};
    do
      echo -ne "\r$i";
      sleep 0.2;
    done;
  done
}


count

sleep 3


pip install pyqrcode

pip install pypng

sleep 2

echo " installing finish " |lolcat
