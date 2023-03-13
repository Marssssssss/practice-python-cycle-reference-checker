# -*- coding:utf-8 -*-

def cycle_reference_checker(obj):
	dfs_stack = [obj]
	dfs_ids = [id(obj)]
	dfs_iters = [iter(getattr(obj, "__dict__", {}).items())]
	dfs_path = ["root"]
	has_cycle = False

	while dfs_stack:
		cur_obj, cur_iter = dfs_stack[-1], dfs_iters[-1]

		try:
			next_key, next_obj = next(cur_iter)
		except StopIteration:
			dfs_stack.pop(-1)
			dfs_iters.pop(-1)
			dfs_path.pop(-1)
			dfs_ids.pop(-1)
			continue

		# check cycle reference
		dfs_path.append(next_key)
		if id(next_obj) in dfs_ids:
			all_cycle_path = ".".join(dfs_path)
			duplicate_path = ".".join(dfs_path[:dfs_stack.index(next_obj) + 1])
			print("cycle reference! ", all_cycle_path, "=", duplicate_path, "type:", type(next_obj), "id:", id(next_obj))

			has_cycle = True
			dfs_path.pop(-1)
			continue

		dfs_stack.append(next_obj)
		dfs_iters.append(iter(getattr(next_obj, "__dict__", {}).items()))
		dfs_ids.append(id(next_obj))

	if not has_cycle:
		print("find no cycle reference!")


class TestCls(object):
	pass


def test_case_no_cycle():
	a = TestCls()
	b = TestCls()
	c = TestCls()

	a.b = b
	a.c = c
	b.c = c

	print(">>>> test case no cycle <<<<")
	cycle_reference_checker(a)
	print("\n")


def test_case_has_cycle():
	a = TestCls()
	b = TestCls()
	c = TestCls()

	a.b = b
	b.c = c
	a.c = c
	c.a = a
	c.b = b

	print(">>>> test case has cycle <<<<")
	cycle_reference_checker(a)
	print("\n")


if __name__ == "__main__":
	test_case_no_cycle()
	test_case_has_cycle()
