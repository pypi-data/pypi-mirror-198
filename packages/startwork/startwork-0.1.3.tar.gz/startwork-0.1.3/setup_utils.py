import re as regex

def clean_up_md(md_string):
	# find badges
	badges_index = {}
	badges_index["start"] = md_string.find("<!-- badges start -->")
	badges_index["end"] = md_string.find("<!-- badges end -->")
	if not badges_index["start"] or not badges_index["end"]:
		raise Exception('badges not found at "README.md"')

	# remove badges
	md_string = md_string[:badges_index["start"]] + md_string[badges_index["end"]:]
	md_string.replace("<!-- badges end -->", "Source code avaliable at: https://github.com/JorbFreire/startwork")

	# remove links
	url_regex = "\[[a-zA-Z]{2,}\]\([a-zA-Z0-9@_#$%&?/\.:]+\)"
	links = regex.findall(url_regex, md_string)
	for link in links:
		link_name = link.split("]")[0].replace("[", "")
		md_string = md_string.replace(link, link_name)

	# simplify code blocks
	code_blocks_regex = "```[a-zA-Z]+\n"
	code_blocks = regex.findall(code_blocks_regex, md_string)
	for code_block in code_blocks:
		md_string = md_string.replace(code_block, "```\n")

	# remove html tags
	md_string = md_string.replace("<br />", "")

	# simplify checkmark list
	md_string = md_string.replace("- [ ]", "- ")
	md_string = md_string.replace("  - [ ]", "\n  - ")
	md_string = md_string.replace("- [x]", "- ✔")
	
	# return end result
	return md_string
