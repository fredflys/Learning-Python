old_dict = {
 "#1":11,
 "#2":22,
 "#3":100,
 "#5":1,}
new_dict = {
 "#1":33,
 "#4":22,
 "#7":200,
 "#5":123,}
#更新old中key键的交集，删除old-new中的差集，添加new-old的差集
#（即更新数据源）
def update_data(old_dict,new_dict):
      old_keys = old_dict.keys()
      new_keys = new_dict.keys()
      #python3中.keys()类型为dict_keys，2中是list，但都可迭代
      old_set = set(old_keys) #123
      new_set = set(new_keys) #147
      #old-new差集,删除
      del_set = old_set.difference(new_set) #23
      #new_old差集，添加
      add_set = new_set.difference(old_set) #47
      #old和new交集，更新
      update_set = old_set.intersection(new_set) #1
      del_items = []
      for d in del_set:
            del_items = old_dict.pop(d)
      for a in add_set:
            old_dict.update({a:new_dict[a]})
      for u in update_set:
            old_dict.update({u:new_dict[u]})

      return old_dict

print(update_data(old_dict,new_dict))
