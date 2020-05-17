mcd(){
	mkdir -p "$1"
	cd "$1"
	echo mantap_men > "$2.txt"
}
echo "berisi fungsi mcd namaFolder namaFile"

# cara memanggil fungsi
# mcd namaFolder namaFile
