def support_bound(sample_size: int) -> float:
	"""
	The bound for a support of NW triangular kernel. 
	:param sample_size: size of a sample for which NW kernel will be used. 
	"""
	bound = sample_size ** (1 / 3)
	return bound
