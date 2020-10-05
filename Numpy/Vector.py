from matplotlib import pyplot as plt

# plt.scatter(35.2, 16.3, c='r')
# plt.scatter(0,0, c='black')
# # plt.xlim(-40,40)
# # plt.ylim(-40,40)
# #
# # plt.grid(True)
# # plt.xlabel('sugar')
# # plt.ylabel('moisture')
# # plt.title('Fruit Figure')
# # plt.show()
# # plt.close()
#
# head_width = 1.6
# width = 0.001
# plt.arrow(0,0,35.2-head_width*2,16.3-head_width*2+1,
#           color = 'black',
#           width=width,
#           head_width=head_width)
#
# plt.xlim(-40,40)
# plt.ylim(-40,40)
#
# plt.grid(True)
# plt.xlabel('sugar')
# plt.ylabel('moisture')
# plt.title('Fruit Figure')
# plt.show()
# plt.close()

ax = plt.figure().gca(projection='3d')
ax.scatter(35.2, 16.3, 25.1, c='r')
ax.scatter(0,0,0,c='black')

head_width =1.6
width = 0.001
ax.plot([0, 35.2], [0, 16.3],[0, 25.1], c='black')
ax.grid(True)
ax.set_xlim([-40,40])
ax.set_ylim([-40,40])
ax.set_zlim([-40,40])
plt.show()
plt.close()
