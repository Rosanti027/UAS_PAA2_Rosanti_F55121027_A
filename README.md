# UAS_PAA2_Rosanti_F55121027_A
# Analysis Algorithm: Bubble sort or insertion sort

Worst Case:
Bubble Sort: Pada worst case, ketika data yang diurutkan dalam keadaan terbalik, Bubble Sort akan memiliki kinerja terburuk. Jumlah iterasi yang dibutuhkan adalah sebanyak n-1 iterasi untuk setiap elemen pada array yang belum terurut. Sehingga kompleksitas waktu Bubble Sort pada worst case adalah O(n^2).
Insertion Sort: Pada worst case, ketika data yang diurutkan dalam keadaan terbalik, Insertion Sort akan memiliki kinerja terburuk. Pada setiap iterasi, Insertion Sort harus memindahkan elemen-elemen yang lebih besar ke posisi yang lebih tinggi dalam array, sehingga kompleksitas waktu Insertion Sort pada worst case adalah O(n^2).

Best Case:
Bubble Sort: Pada best case, ketika data yang diurutkan sudah dalam keadaan terurut secara ascending, Bubble Sort akan memiliki kinerja terbaik. Namun, meskipun data sudah terurut, Bubble Sort tetap akan melakukan n-1 iterasi untuk memastikan bahwa array sudah benar-benar terurut. Sehingga kompleksitas waktu Bubble Sort pada best case tetap adalah O(n^2).
Insertion Sort: Pada best case, ketika data yang diurutkan sudah dalam keadaan terurut secara ascending, Insertion Sort akan memiliki kinerja terbaik. Setiap elemen hanya perlu dibandingkan dengan elemen sebelumnya dan tidak ada perluasan array yang diperlukan. Sehingga kompleksitas waktu Insertion Sort pada best case adalah O(n).

Average Case:
Bubble Sort: Pada average case, kompleksitas waktu Bubble Sort adalah O(n^2), karena setiap elemen membutuhkan n-1 iterasi dalam rata-rata untuk mencapai posisi yang benar.
Insertion Sort: Pada average case, kompleksitas waktu Insertion Sort adalah O(n^2), karena setiap elemen membutuhkan sekitar n/2 iterasi dalam rata-rata untuk mencapai posisi yang benar.


 
 
# Analysis Algorithm: TSP dan Dijkstra's
a. Worst Case:
TSP: Pada worst case, kompleksitas waktu algoritma TSP adalah O(n!), di mana n adalah jumlah simpul dalam graf. Hal ini terjadi ketika semua kemungkinan permutasi jalur harus diperiksa.
Dijkstra's Algorithm: Pada worst case, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam graf. Hal ini terjadi ketika harus diperiksa semua simpul dan tepi dalam graf.

b. Best Case:
TSP: Pada best case, ketika graf memiliki jumlah simpul yang sedikit, kompleksitas waktu algoritma TSP dapat didekati sebagai O(1).
Dijkstra's Algorithm: Pada best case, kompleksitas waktu algoritma Dijkstra adalah O(V log V), di mana V adalah jumlah simpul dalam graf. Hal ini terjadi ketika simpul awal adalah tujuan akhir atau terdapat jalur terpendek langsung dari simpul awal ke tujuan akhir.

c. Average Case:
TSP: Algoritma TSP memiliki kompleksitas waktu rata-rata sekitar O(n!) karena harus memeriksa sebagian besar permutasi jalur.
Dijkstra's Algorithm: Algoritma Dijkstra memiliki kompleksitas waktu rata-rata sekitar O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam graf. Hal ini dapat bervariasi tergantung pada struktur graf.
Perlu diingat bahwa analisis ini hanya memberikan perkiraan dan kompleksitas waktu yang sebenarnya dapat dipengaruhi oleh faktor-faktor lain seperti implementasi dan ukuran graf.
