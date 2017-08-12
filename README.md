# singing voice separation 朱恺康
Intro:
  My project is singing voice separation,it is based on the code from my teacher Dr.Zhang Xulong and some examples searched on the Internet.
  
Experiments:
	They are based on the "REPET-SIM"method of  Rafii and Pardo, 2012, but includes a couple of modifications and extensions:
 	FFT windows overlap by 1/4, instead of 1/2
 	Non-local filtering is converted into a soft mask by Wiener filtering. This is similar in spirit to the soft-masking method used by Fitzgerald, 2012, but is a bit more numerically stable in practice.
  
To evaluate the effect of the method,evaluation()is added by using mir-eval.It can show the values of sdr, sir, sar, perm.

References:
 Rafii Pardo, Music-Voice Separation using the Similarity Matrix, ISMIR,2012
 /nFitzgerald, D. (2012) Vocal separation using nearest neighbours and median filtering. 23rd IET Irish Signals and Systems Conference,
Maynooth. 28-29th. June 2012.
