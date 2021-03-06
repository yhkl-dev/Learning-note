#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TElementType char

typedef enum {Link, Thread} PointerTag;

typedef struct biThrNode {
	TElementType data;
	struct biThrNode *left, *right;
	PointerTag leftTag;
	PointerTag rightTag;
} biThrNode, *biThrTree;

biThrTree pre;

int main() {
	return 0;
}

void inTreading(biThrTree p) {
	if (p) {
		inTreading(p->left);
		if (!p->left) {
			p->leftTag = Thread;
			p->left = pre;
		}
		if (!p->right) {
			pre->rightTag = Thread;
			pre->right = p;
		}
		pre = p;
		inTreading(p->right);
	}
}

bool inOrderTraverseTree(biThrTree T) {
	biThrTree p;
	p = T->left;
	while (p != T) {
		while (p->leftTag == Link) {
			p = p->left;
		}
		printf("%c", p->data);
		while (p->rightTag == Thread && p->right != T) {
			p = p->right;
			printf("%c", p->data);
		}
		p = p->left;
	}
	return true;
}






















