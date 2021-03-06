@pytest.mark.android
@pytest.mark.time_test
@pytest.mark.interface
def test_time_selector(driver):
    # Getting to the dialog...
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Date Widgets").click()
    driver.find_element_by_accessibility_id("1. Dialog").click()
    # Getting the initial time from the datetime string...
    initial_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    initial_time = initial_date_display[1].split(":")
    # Opening the Set time dialog
    driver.find_element_by_accessibility_id("change the time").click()
    # Wait for the dialog to appear
    driver.implicitly_wait(5)
    # Save initial settings...
    initial_hours = driver.find_element_by_id("android:id/hours").text
    initial_minutes = driver.find_element_by_id("android:id/minutes").text
    # Convert str to int so we don't have to deal with leading zero
    # Check that it's the same time as we got from the previous screen
    assert int(initial_hours) == int(initial_time[0])
    assert int(initial_minutes) == int(initial_time[1])
    driver.find_element_by_accessibility_id("7").click()  # Set new hours value
    driver.find_element_by_accessibility_id("40").click()  # Set new minutes value
    new_hours = driver.find_element_by_id("android:id/hours").text  # Get new hour setting
    new_minutes = driver.find_element_by_id("android:id/minutes").text  # Get new minutes setting
    assert new_hours == "7"  # Hours set correctly?
    assert new_minutes == "40"  # Minutes set correctly?
    # Just print the time.
    time_header = driver.find_element_by_id("android:id/time_header").text
    print(time_header)
    # Close the dialog
    driver.find_element_by_id("android:id/button1").click()
    # Get the time portion of datetime display and split it
    result_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    result_time = result_date_display[1].split(":")
    assert int(new_hours) == int(result_time[0])  # Hours set correctly?
    assert int(new_minutes) == int(result_time[1])  # Minutes set correctly?


@pytest.mark.android
@pytest.mark.date_test
@pytest.mark.interface
def test_date_selector(driver):
    # Getting to the dialog...
    # pdb.set_trace()
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Date Widgets").click()
    driver.find_element_by_accessibility_id("1. Dialog").click()
    # Getting the initial time from the datetime string...
    [initial_month, initial_day, initial_year] = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")[0].split("-")
    print("Month #", initial_month)
    # Opening the Set time dialog
    driver.find_element_by_accessibility_id("change the date").click()
    # Wait for the dialog to appear
    driver.implicitly_wait(5)
    # Save initial settings...
    initial_hours = driver.find_element_by_id("android:id/hours").text
    initial_minutes = driver.find_element_by_id("android:id/minutes").text
    # Convert str to int so we don't have to deal with leading zero
    # Check that it's the same time as we got from the previous screen
    assert int(initial_hours) == int(initial_date)
    assert int(initial_minutes) == int(initial_time[1])
    driver.find_element_by_accessibility_id("7").click()  # Set new hours value
    driver.find_element_by_accessibility_id("40").click()  # Set new minutes value
    new_hours = driver.find_element_by_id("android:id/hours").text  # Get new hour setting
    new_minutes = driver.find_element_by_id("android:id/minutes").text  # Get new minutes setting
    assert new_hours == "7"  # Hours set correctly?
    assert new_minutes == "40"  # Minutes set correctly?
    # Just print the time.
    time_header = driver.find_element_by_id("android:id/time_header").text
    print(time_header)
    # Close the dialog
    driver.find_element_by_id("android:id/button1").click()
    # Get the time portion of datetime display and split it
    result_date_display = driver.find_element_by_id("io.appium.android.apis:id/dateDisplay").text.split(" ")
    result_time = result_date_display[1].split(":")
    assert int(new_hours) == int(result_time[0])  # Hours set correctly?
    assert int(new_minutes) == int(result_time[1])  # Minutes set correctly?
