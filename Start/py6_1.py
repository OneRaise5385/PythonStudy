# 字典

alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'slow'
print(alien_0)
if alien_0['speed'] == 'slow':
    alien_0['speed'] = 'medium'
print('speed: ' + alien_0['speed'])
print('points: ' + str(alien_0['points']))

# 删除键值对
del alien_0['speed']
print(alien_0)

# 由类似对象组成的字典
favorite_languages = {
    'zhang':'Python',
    'wang':'C',
    'li':'Python',
    'zhao':'Java'
}
print("Zhang's fovorite language is " +
      favorite_languages['zhang'] +
      '.')