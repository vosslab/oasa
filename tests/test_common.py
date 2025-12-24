#!/usr/bin/env python3

import oasa.common as common


#============================================
def main():
	result = common.is_uniquely_sorted([1, 2, 3])
	assert result is True

	result = common.is_uniquely_sorted([1, 2, 2, 3])
	assert result is False


if __name__ == '__main__':
	main()
