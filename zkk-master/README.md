# singing voice separation 朱恺康
Intro
	现如今，信息化的程度越来越高，音乐信息在总的信息中所占的比重不断增大，从音乐中提取有用信息（Music Information Retrieval）变得越发重要。我所做的项目是音乐分离
 参照了张旭龙老师的音乐分离代码和网上的一些例子。
experiments
	They are based on the "REPET-SIM"method of  Rafii and Pardo, 2012, but includes a couple of modifications and extensions:

	FFT windows overlap by 1/4, instead of 1/2
	Non-local filtering is converted into a soft mask by Wiener filtering. This is similar in spirit to the soft-masking method used by Fitzgerald, 2012, but is a bit more numerically stable in practice.
To evaluate the effect of the method,evaluation()is added by using mir-eval.It can show the values of sdr, sir, sar, perm.