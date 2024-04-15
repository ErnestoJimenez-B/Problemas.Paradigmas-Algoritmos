#include <iostream>

using namespace std;
int floorSqrt(int x)
{
	// Casos
	if (x == 0 || x == 1)
		return x;

	// Busqueda Binaria
	int start = 1, end = x / 2, ans;
	while (start <= end) {
		int mid = (start + end) / 2;

		// Cuadrado perfecto
		int sqr = mid * mid;
		if (sqr == x)
			return mid;

		// mid*mid<x
		if (sqr <= x) {
			start = mid + 1;
			ans = mid;
		}
		else // mid*mid>x
			end = mid - 1;
	}
	return ans;
}
int main()
{
	int x = 11;
	cout << floorSqrt(x) << endl;
	return 0;
}
