import uiautomator2 as u2
import sys
import time
d(resourceId="com.amaze.filemanager:id/sd_main_fab").click()
d.xpath('//*[@resource-id="com.amaze.filemanager:id/menu_new_file"]/android.widget.ImageButton[1]').click()
d.swipe(0.133, 0.262, 0.213, 0.264)
d(resourceId="android:id/floating_toolbar_menu_item_text", text="Cut").click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_7"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_bottom_symbol_2"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_shift"]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_4"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_4"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_1"]/android.widget.TextView[1]').click()
d(resourceId="com.amaze.filemanager:id/md_buttonDefaultPositive").click()
d(resourceId="com.amaze.filemanager:id/search").click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_shift"]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_7"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_bottom_symbol_2"]/android.widget.TextView[1]').click()
d.xpath('//android.widget.TextView').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_4"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_4"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_1"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]/android.widget.ImageView[2]').click()
d(resourceId="com.amaze.filemanager:id/properties").click()
d.swipe(0.846, 0.735, 0.86, 0.484)
d.xpath('//android.widget.ListView/android.widget.LinearLayout[8]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()

while True:
    d.service("uiautomator").stop()
    time.sleep(2)
    out = d.service("uiautomator").running()
    if not out:
        print("DISCONNECT UIAUTOMATOR2 SUCCESS")
        break
    time.sleep(2)