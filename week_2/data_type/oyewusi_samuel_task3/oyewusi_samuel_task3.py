# # 1 
# surname = input("Enter your surname name: ")
# print(surname.upper())

# # 2
# word = "python"
# print(" first charact is", word[0],  ", \n last character is", word[-1])

# # 3
# name = input("Enter your name: ")
# print("Hello, !", name)

# 4
# text = "welcome to python"
# print(text.find(text[-1]))

# # 5
# word_2 = "Hello world"
# new_word_2 = word_2.replace("world", "python")
# print(new_word_2)

# # 6 
# print("python" in new_word_2)

# # 7
# a ="Hello"
# print(a[-1:-6:-1])

# # 8
# word_2 = "  Hello world  "
# print(word_2.strip())

# 9
vowel_count = input("Enter a sentence: ")
a = vowel_count.count("a")
e = vowel_count.count("e")
i = vowel_count.count("i")
o = vowel_count.count("o")
u = vowel_count.count("u")
A = vowel_count.count("A")
E = vowel_count.count("E")
I = vowel_count.count("I")
O = vowel_count.count("O")
U = vowel_count.count("U")
total_vowel = a+e+i+o+u+A+E+I+O+U
print("The total vowel in your sentence is:", total_vowel)

# # 10
# string_1 = "1234"
# conv_str = int(string_1) * 2
# print(conv_str)

# # 11
# string_2 = "apple,banana,orange"
# print(string_2.split(","))

# # 12
# user_input = input("Enter a sentence: ")
# input_conv = user_input.split()
# print("\n".join(input_conv))

# # 13
# string_3 = "Hello user welcome"
# print(string_3.replace(" ", "_"))

# # 14
# string_4 = "banana"
# string_count = string_4.count("a")
# print(string_count)

# # 15
# string_4 = "https://facebook.com"
# print(string_4.startswith("https://"))
