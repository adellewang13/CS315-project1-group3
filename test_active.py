from page_objects.PageTiktok import PageTiktok
import time

def test_like_hashtag():
    # login with your active tiktok account
    scenario_num = 2 #change this number here for different scenarios!
    username = "Sec01Gr3Sc2Activ_RX"#replace JL with your initial
    page = PageTiktok(scenario_num,username)
    page.fetch_tiktok()
    time.sleep(60)
    page.iterate_through_batches_like_by_hashtag()
    #page.chromebrowser.delete_all_cookies()
    time.sleep(10)


