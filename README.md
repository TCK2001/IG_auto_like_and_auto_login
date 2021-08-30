## IG_auto_like_and_auto_login
-----
```python
while True:
    # click like
    xpath="//article//section/span/button"
    driver.find_elements_by_xpath(xpath)[0].click()
    time.sleep(1+random.random())

    # next page
     xpath2="//a"
     el_list=driver.find_elements_by_xpath(xpath2)
     for el in el_list:
         if el.text=="다음":
             el.click()
             break
     time.sleep(3+random.random())
```
+ This part is auto like in instagram.
+ But you have to log_in first and use jupyter to compile the code.
```python
time.sleep(3+random.random())
```
+ This is protect ben for instagram program.
--------
+ The rest of the code is similar to the Facebook automatic login I posted in the past.
