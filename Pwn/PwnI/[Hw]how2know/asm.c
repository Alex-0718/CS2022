#include <stdbool.h>
#include <stdio.h>

static char flag[0x30] = "FLAG{NEVER_LOSES_87}";
int main() {
    register int index, character;
	register int run;
	register char c;
	register char* p;

	p = flag;
	c = *(p + index);
	run = c < character;
	while (run) { // spin
	}
}