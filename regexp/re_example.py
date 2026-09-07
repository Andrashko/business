import re
HTML = """
<div class="page front">
    <div class="band header_front">
        <div class="container header-container">
            <header class="six columns header-brand">
                <a href="https://uzhnu.edu.ua/en/">
                    <img class="header-brand__logo" src="/images/layout/UzNU_logo_new-header.png" alt="Логотип УжНУ">
                    <h1 class="header-brand__title">Uzhhorod National University</h1>
                </a>
            </header>

            <div class="six columns header-utility">
                <ul class="iconset flags_icons">
                    <li><a class="uk" href="/uk/">uk</a></li><li><a class="en" href="/en/">en</a></li>                </ul>
                <div class="clearfix"></div>

                <div class="topmenu" style="padding-top: 37px;">
                    <a href="#" class="btn-mobile-menu js-btn-mobile-menu" style="top: 47px;"><i class="fa fa-bars"></i></a>
                    



<div id="searchwrapper">
<form style="inline" id="search-form" action="/en/search/" method="get">
    <input placeholder="пошук..." type="text" value="" name="q" id="q">    <input style="width:38px;height:22px" src="/images/icons/blank.gif" type="image" name="yt0">
</form></div>                    <div class="clearfix"></div>


                    
                        <ul class="header-utility__quickmenu" id="yw2">
<li><a href="/en/">Home</a> |</li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/s_subdivisions-dep_personal/vacancies">Vacancies</a> |</li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/10741">E-mail</a> |</li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/22606">Technical support</a> |</li>
<li><a href="/en/cat/general_pages/contacts">Contacts</a> |</li>
<li><a href="/en/site/login">Login </a></li>
</ul>
                        
                </div>



            </div>  <!--seven columns  -->
        </div> <!-- container header -->
    </div> <!-- band header -->

    <div class="band navigation">

                    <nav class="container">
                <div class="twelve columns menu-desktop" id="sf_mainmenu">
                    <ul id="yw3" class="sf-menu sf-js-enabled sf-arrows">
<li><a href="#" class="sf-with-ul">UzhNU</a>
<ul style="display: none;">
<li><a href="https://www.uzhnu.edu.ua/uk/news/"><span>- </span>News</a></li>
<li><a href="/en/cat/university-about_us" class="sf-with-ul"><span>- </span>Presentations</a>
<ul style="display: none;">
<li><a href="/en/cat/about_us-video"><span>--- </span>Video about faculties</a></li>
</ul>
</li>
<li><a href="/en/cat/university-directors"><span>- </span>University Administration</a></li>
<li><a href="/en/cat/university-council"><span>- </span>Specialized Academic   Council</a></li>
<li><a href="/en/cat/university-history"><span>- </span>History</a></li>
<li><a href="/en/cat/university-symbols"><span>- </span>Symbols</a></li>
<li><a href="/en/cat/general_pages/univ_structure"><span>- </span>Structural units</a></li>
<li><a href="/en/cat/university-museums" class="sf-with-ul"><span>- </span>Museums</a>
<ul style="display: none;">
<li><a href="/en/cat/museums-zoo_museum"><span>--- </span>Zoological Museum of UzhNU</a></li>
<li><a href="/en/cat/museums-history_mus"><span>--- </span>Museum of UzhNU History </a></li>
<li><a href="/en/cat/museums-arich_muz"><span>--- </span>Archeological Museum of UzhNU</a></li>
<li><a href="/en/cat/museums-bot_garden"><span>--- </span>Botanical Garden of UzhNU</a></li>
</ul>
</li>
<li><a href="/en/news/cat/media_about_us"><span>- </span>Media about UzhNU</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/infocentre/450"><span>- </span>Regulatory Documents</a></li>
<li><a href="/en/cat/general_pages/public_info"><span>- </span>Access to public information</a></li>
<li><a href="/en/cat/university-dev_strategy"><span>- </span>Concept Strategy</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/10568"><span>- </span>Supervisory Board</a></li>
<li><a href="/en/cat/university-volunteerism"><span>- </span>Volunteerism</a></li>
<li><a href="/en/cat/university-int_alum_assoc"><span>- </span>International Alumni Association</a></li>
<li><a href="/en/cat/university-policy_of_ssd" class="sf-with-ul"><span>- </span>Policy of the Resilience and Sustainable Development</a>
<ul style="display: none;">
<li><a href="/en/cat/policy_of_ssd-sust_dev"><span>--- </span>Sustainability Development Centre</a></li>
<li><a href="/en/cat/policy_of_ssd-gender_center"><span>--- </span>Center for gender education</a></li>
<li><a href="/en/cat/policy_of_ssd-mizhdysc"><span>--- </span>Center for Interdisciplinary Scientific Research</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="/en/cat/abiturient" class="sf-with-ul">For University Entrants</a>
<ul style="display: none;">
<li><a href="https://www.uzhnu.edu.ua/uk/cat/abiturient/about"><span>- </span>Entrants</a></li>
<li><a href="https://vstup.uzhnu.edu.ua/calculator"><span>- </span></a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/abiturient/presentations"><span>- </span>About the University</a></li>
<li><a href="/en/cat/faculty"><span>- </span>Faculties</a></li>
<li><a href="/en/cat/abiturient-foreign" class="sf-with-ul"><span>- </span>For foreign students</a>
<ul style="display: none;">
<li><a href="/en/cat/foreign-representatives"><span>--- </span>Representatives</a></li>
<li><a href="/en/cat/foreign-acc_activation"><span>--- </span>University Account activation</a></li>
<li><a href="https://docs.google.com/forms/d/1zIsUEo9G5Vhd_zhWZvgaEeMCylfTLb-36Lmv5kNgXFQ/edit?ts=6731e3e9"><span>--- </span>Admission form</a></li>
</ul>
</li>
<li><a href="/en/cat/university-humanitar" class="sf-with-ul"><span>- </span>Ukrainian-Hungarian educational institute</a>
<ul style="display: none;">
<li><a href="/en/cat/humanitar-hu_history"><span>--- </span>Department of the History of Hungary and European Integration</a></li>
<li><a href="/en/cat/humanitar-hu_filology"><span>--- </span>Department of Hungarian Philology </a></li>
<li><a href="/en/cat/humanitar-hu_fizmath"><span>--- </span>Department of  Physics and Mathematics </a></li>
<li><a href="/en/cat/humanitar-centre_hungary"><span>--- </span>Hungarology Center</a></li>
</ul>
</li>
<li><a href="/en/cat/university-college"><span>- </span>College</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/15068"><span>- </span>Educational programs</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/programs"><span>- </span>Specialities / Educational programs</a></li>
</ul>
</li>
<li><a href="#" class="sf-with-ul">For students</a>
<ul style="display: none;">
<li><a href="/en/cat/faculty"><span>- </span>Faculties</a></li>
<li><a href="/en/cat/university-humanitar" class="sf-with-ul"><span>- </span>Ukrainian-Hungarian educational institute</a>
<ul style="display: none;">
<li><a href="/en/cat/humanitar-hu_history"><span>--- </span>Department of the History of Hungary and European Integration</a></li>
<li><a href="/en/cat/humanitar-hu_filology"><span>--- </span>Department of Hungarian Philology </a></li>
<li><a href="/en/cat/humanitar-hu_fizmath"><span>--- </span>Department of  Physics and Mathematics </a></li>
<li><a href="/en/cat/humanitar-centre_hungary"><span>--- </span>Hungarology Center</a></li>
</ul>
</li>
<li><a href="/en/cat/university-college"><span>- </span>College</a></li>
<li><a href="/en/cat/university-dwise_training" class="sf-with-ul"><span>- </span>Department of Wise Training</a>
<ul style="display: none;">
<li><a href="/en/cat/dwise_training-help_ato"><span>--- </span></a></li>
</ul>
</li>
<li><a href="https://rozklad.uzhnu.edu.ua/"><span>- </span>Electronic schedule</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-aspirant"><span>- </span>PhD and Doctorate programmes</a></li>
<li><a href="/en/cat/university-int_alum_assoc"><span>- </span>International Alumni Association</a></li>
<li><a href="/en/cat/student-self_government"><span>- </span>Student Council</a></li>
<li><a href="/en/cat/student-nauk_tov"><span>- </span>Scientific Society</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/s_subdivisions-dep_hum_ed_work"><span>- </span>Department of Humanitarian and educational work</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/dep_hum_ed_work-employment"><span>- </span>Employment</a></li>
<li><a href="/en/cat/student-sportandleasure"><span>- </span>Sport &amp; Leisure</a></li>
<li><a href="/en/cat/student-career_center"><span>- </span>Career Center</a></li>
<li><a href="/en/cat/educ_dep-dep_stud"><span>- </span>Student Department</a></li>
<li><a href="/en/cat/s_subdivisions-stud_union_comm"><span>- </span>Students' professional union</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/15068"><span>- </span>Educational programs</a></li>
<li><a href="/en/cat/student-public_lectures"><span>- </span>Public lectures</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/deps-ndc_innov_rozv/events"><span>- </span>Scientific guide</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/abiturient-foreign"><span>- </span>For foreign students</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/40666"><span>- </span>Catalog of elective disciplines</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/33387"><span>- </span> Social scholarship</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/university-driving_school"><span>- </span>Driving school</a></li>
</ul>
</li>
<li><a href="#" class="sf-with-ul">Science</a>
<ul style="display: none;">
<li><a href="/uk/cat/science-atest_kom"><span>- </span>Attestation commission</a></li>
<li><a href="https://www.lib.uzhnu.edu.ua/"><span>- </span>Scientific Library</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/student-nauk_tov"><span>- </span>Scientific Society of Students and Graduate Students</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/deps-ndc_innov_rozv/events"><span>- </span>Scientific guide</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/33564"><span>- </span>Scientific professional publications UzhNU</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-ndch"><span>- </span>Research part</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-deps"><span>- </span>Research institutes, centers and laboratories</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-resources"><span>- </span>Scientific and informational resources</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-scientific_coun"><span>- </span>Scientific and technical council</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-cou_of_youn_sci"><span>- </span>The Young Scientists Council</a></li>
<li><a href="#" class="sf-with-ul"><span>- </span>Editorial and publishing activity</a>
<ul style="display: none;">
<li><a href="https://uzhnu.edu.ua/uk/cat/edit_publ-red_rada"><span>--- </span>Editorial and publishing council</a></li>
<li><a href="https://uzhnu.edu.ua/uk/cat/edit_publ-ed_pub_dep"><span>--- </span>Editorial and publishing department</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/67561"><span>--- </span>Scientific publications</a></li>
<li><a href="https://uzhnu.edu.ua/uk/infocentre/53409"><span>--- </span></a></li>
</ul>
</li>
<li><a href="/uk/cat/science-vch_sekr"><span>- </span></a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-science_spec_sc"><span>- </span>Specialized scientific councils</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-center_pak"><span>- </span>Center for training and certification of highly qualified personnel</a></li>
<li><a href="/uk/cat/deps-startup_centre"><span>- </span></a></li>
</ul>
</li>
<li><a href="/en/cat/irelations" class="sf-with-ul">International Activities</a>
<ul style="display: none;">
<li><a href="/en/cat/irelations-dep_irelations"><span>- </span>The Department of International Relations</a></li>
<li><a href="/en/cat/irelations-partners"><span>- </span>Our Partners</a></li>
<li><a href="/en/cat/irelations-ir_grants"><span>- </span>Search for Grants  and Scholarships</a></li>
<li><a href="/en/cat/irelations-projects"><span>- </span>Educational and Institutional International Projects</a></li>
<li><a href="http://erasmusplus.uzhnu.edu.ua/"><span>- </span>Erasmus+ Educational Programmes</a></li>
<li><a href="/en/cat/irelations-double_diploms"><span>- </span>Semester Abroad Study and Joint Programmes</a></li>
</ul>
</li>
<li><a href="#" class="sf-with-ul">Projects</a>
<ul style="display: none;">
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-cat_grants/grant"><span>- </span>Search for grants and scholarships</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/irelations-projects"><span>- </span>International educational and institutional projects</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-cat_grants/completed_grants"><span>- </span>International scientific projects</a></li>
</ul>
</li>
</ul>                </div>

                <div class="menu-mobile js-menu-mobile">
                    <div class="menu-mobile__utils">
                        <a href="#" class="menu-mobile__close-btn js-btn-mobile-menu-close"><i class="fa fa-times"></i></a>
                    </div>
                    <ul class="menu-mobile__menu js-menu-mobile__menu" id="yw4">
<li><a href="#">UzhNU</a>
<ul>
<li><a href="https://www.uzhnu.edu.ua/uk/news/"><span>- </span>News</a></li>
<li><a href="/en/cat/university-about_us"><span>- </span>Presentations</a>
<ul>
<li><a href="/en/cat/about_us-video"><span>--- </span>Video about faculties</a></li>
</ul>
</li>
<li><a href="/en/cat/university-directors"><span>- </span>University Administration</a></li>
<li><a href="/en/cat/university-council"><span>- </span>Specialized Academic   Council</a></li>
<li><a href="/en/cat/university-history"><span>- </span>History</a></li>
<li><a href="/en/cat/university-symbols"><span>- </span>Symbols</a></li>
<li><a href="/en/cat/general_pages/univ_structure"><span>- </span>Structural units</a></li>
<li><a href="/en/cat/university-museums"><span>- </span>Museums</a>
<ul>
<li><a href="/en/cat/museums-zoo_museum"><span>--- </span>Zoological Museum of UzhNU</a></li>
<li><a href="/en/cat/museums-history_mus"><span>--- </span>Museum of UzhNU History </a></li>
<li><a href="/en/cat/museums-arich_muz"><span>--- </span>Archeological Museum of UzhNU</a></li>
<li><a href="/en/cat/museums-bot_garden"><span>--- </span>Botanical Garden of UzhNU</a></li>
</ul>
</li>
<li><a href="/en/news/cat/media_about_us"><span>- </span>Media about UzhNU</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/infocentre/450"><span>- </span>Regulatory Documents</a></li>
<li><a href="/en/cat/general_pages/public_info"><span>- </span>Access to public information</a></li>
<li><a href="/en/cat/university-dev_strategy"><span>- </span>Concept Strategy</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/10568"><span>- </span>Supervisory Board</a></li>
<li><a href="/en/cat/university-volunteerism"><span>- </span>Volunteerism</a></li>
<li><a href="/en/cat/university-int_alum_assoc"><span>- </span>International Alumni Association</a></li>
<li><a href="/en/cat/university-policy_of_ssd"><span>- </span>Policy of the Resilience and Sustainable Development</a>
<ul>
<li><a href="/en/cat/policy_of_ssd-sust_dev"><span>--- </span>Sustainability Development Centre</a></li>
<li><a href="/en/cat/policy_of_ssd-gender_center"><span>--- </span>Center for gender education</a></li>
<li><a href="/en/cat/policy_of_ssd-mizhdysc"><span>--- </span>Center for Interdisciplinary Scientific Research</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="/en/cat/abiturient">For University Entrants</a>
<ul>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/abiturient/about"><span>- </span>Entrants</a></li>
<li><a href="https://vstup.uzhnu.edu.ua/calculator"><span>- </span></a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/abiturient/presentations"><span>- </span>About the University</a></li>
<li><a href="/en/cat/faculty"><span>- </span>Faculties</a></li>
<li><a href="/en/cat/abiturient-foreign"><span>- </span>For foreign students</a>
<ul>
<li><a href="/en/cat/foreign-representatives"><span>--- </span>Representatives</a></li>
<li><a href="/en/cat/foreign-acc_activation"><span>--- </span>University Account activation</a></li>
<li><a href="https://docs.google.com/forms/d/1zIsUEo9G5Vhd_zhWZvgaEeMCylfTLb-36Lmv5kNgXFQ/edit?ts=6731e3e9"><span>--- </span>Admission form</a></li>
</ul>
</li>
<li><a href="/en/cat/university-humanitar"><span>- </span>Ukrainian-Hungarian educational institute</a>
<ul>
<li><a href="/en/cat/humanitar-hu_history"><span>--- </span>Department of the History of Hungary and European Integration</a></li>
<li><a href="/en/cat/humanitar-hu_filology"><span>--- </span>Department of Hungarian Philology </a></li>
<li><a href="/en/cat/humanitar-hu_fizmath"><span>--- </span>Department of  Physics and Mathematics </a></li>
<li><a href="/en/cat/humanitar-centre_hungary"><span>--- </span>Hungarology Center</a></li>
</ul>
</li>
<li><a href="/en/cat/university-college"><span>- </span>College</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/15068"><span>- </span>Educational programs</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/programs"><span>- </span>Specialities / Educational programs</a></li>
</ul>
</li>
<li><a href="#">For students</a>
<ul>
<li><a href="/en/cat/faculty"><span>- </span>Faculties</a></li>
<li><a href="/en/cat/university-humanitar"><span>- </span>Ukrainian-Hungarian educational institute</a>
<ul>
<li><a href="/en/cat/humanitar-hu_history"><span>--- </span>Department of the History of Hungary and European Integration</a></li>
<li><a href="/en/cat/humanitar-hu_filology"><span>--- </span>Department of Hungarian Philology </a></li>
<li><a href="/en/cat/humanitar-hu_fizmath"><span>--- </span>Department of  Physics and Mathematics </a></li>
<li><a href="/en/cat/humanitar-centre_hungary"><span>--- </span>Hungarology Center</a></li>
</ul>
</li>
<li><a href="/en/cat/university-college"><span>- </span>College</a></li>
<li><a href="/en/cat/university-dwise_training"><span>- </span>Department of Wise Training</a>
<ul>
<li><a href="/en/cat/dwise_training-help_ato"><span>--- </span></a></li>
</ul>
</li>
<li><a href="https://rozklad.uzhnu.edu.ua/"><span>- </span>Electronic schedule</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-aspirant"><span>- </span>PhD and Doctorate programmes</a></li>
<li><a href="/en/cat/university-int_alum_assoc"><span>- </span>International Alumni Association</a></li>
<li><a href="/en/cat/student-self_government"><span>- </span>Student Council</a></li>
<li><a href="/en/cat/student-nauk_tov"><span>- </span>Scientific Society</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/s_subdivisions-dep_hum_ed_work"><span>- </span>Department of Humanitarian and educational work</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/dep_hum_ed_work-employment"><span>- </span>Employment</a></li>
<li><a href="/en/cat/student-sportandleasure"><span>- </span>Sport &amp; Leisure</a></li>
<li><a href="/en/cat/student-career_center"><span>- </span>Career Center</a></li>
<li><a href="/en/cat/educ_dep-dep_stud"><span>- </span>Student Department</a></li>
<li><a href="/en/cat/s_subdivisions-stud_union_comm"><span>- </span>Students' professional union</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/15068"><span>- </span>Educational programs</a></li>
<li><a href="/en/cat/student-public_lectures"><span>- </span>Public lectures</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/deps-ndc_innov_rozv/events"><span>- </span>Scientific guide</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/abiturient-foreign"><span>- </span>For foreign students</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/40666"><span>- </span>Catalog of elective disciplines</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/33387"><span>- </span> Social scholarship</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/university-driving_school"><span>- </span>Driving school</a></li>
</ul>
</li>
<li><a href="#">Science</a>
<ul>
<li><a href="/uk/cat/science-atest_kom"><span>- </span>Attestation commission</a></li>
<li><a href="https://www.lib.uzhnu.edu.ua/"><span>- </span>Scientific Library</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/student-nauk_tov"><span>- </span>Scientific Society of Students and Graduate Students</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/deps-ndc_innov_rozv/events"><span>- </span>Scientific guide</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/33564"><span>- </span>Scientific professional publications UzhNU</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-ndch"><span>- </span>Research part</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-deps"><span>- </span>Research institutes, centers and laboratories</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-resources"><span>- </span>Scientific and informational resources</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-scientific_coun"><span>- </span>Scientific and technical council</a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-cou_of_youn_sci"><span>- </span>The Young Scientists Council</a></li>
<li><a href="#"><span>- </span>Editorial and publishing activity</a>
<ul>
<li><a href="https://uzhnu.edu.ua/uk/cat/edit_publ-red_rada"><span>--- </span>Editorial and publishing council</a></li>
<li><a href="https://uzhnu.edu.ua/uk/cat/edit_publ-ed_pub_dep"><span>--- </span>Editorial and publishing department</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/infocentre/get/67561"><span>--- </span>Scientific publications</a></li>
<li><a href="https://uzhnu.edu.ua/uk/infocentre/53409"><span>--- </span></a></li>
</ul>
</li>
<li><a href="/uk/cat/science-vch_sekr"><span>- </span></a></li>
<li><a href="http://www.uzhnu.edu.ua/uk/cat/science-science_spec_sc"><span>- </span>Specialized scientific councils</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-center_pak"><span>- </span>Center for training and certification of highly qualified personnel</a></li>
<li><a href="/uk/cat/deps-startup_centre"><span>- </span></a></li>
</ul>
</li>
<li><a href="/en/cat/irelations">International Activities</a>
<ul>
<li><a href="/en/cat/irelations-dep_irelations"><span>- </span>The Department of International Relations</a></li>
<li><a href="/en/cat/irelations-partners"><span>- </span>Our Partners</a></li>
<li><a href="/en/cat/irelations-ir_grants"><span>- </span>Search for Grants  and Scholarships</a></li>
<li><a href="/en/cat/irelations-projects"><span>- </span>Educational and Institutional International Projects</a></li>
<li><a href="http://erasmusplus.uzhnu.edu.ua/"><span>- </span>Erasmus+ Educational Programmes</a></li>
<li><a href="/en/cat/irelations-double_diploms"><span>- </span>Semester Abroad Study and Joint Programmes</a></li>
</ul>
</li>
<li><a href="#">Projects</a>
<ul>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-cat_grants/grant"><span>- </span>Search for grants and scholarships</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/irelations-projects"><span>- </span>International educational and institutional projects</a></li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/science-cat_grants/completed_grants"><span>- </span>International scientific projects</a></li>
</ul>
</li>
</ul>                </div>
            </nav>
            
            
    </div> <!-- band navigation -->


    








    
<div class="band content">

    
    <div class="band front_slideshow">
        <div class="container">
            <div class="twelve columns">
                



<div id="hero-slider" class="flexslider">

<div class="flex-viewport" style="overflow: hidden; position: relative;"><ul class="slides" style="width: 1400%; transition-duration: 0.4s; transform: translate3d(-2400px, 0px, 0px);"><li class="clone" style="width: 1200px; float: left; display: block;">
<div id="flexslide-block-slide5">
<a href="/en/news/vid-lejtenanta-do-majora-zsu.htm"><img src="/uploads/news/20250129_1434_fa09314c-40a8-42cc-97f3-8b381ef18ecb_bnr.jpeg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/vid-lejtenanta-do-majora-zsu.htm">Від лейтенанта до майора ЗСУ: історія служби директора Центру доуніверситетської підготовки та роботи з іноземними громадянами УжНУ Владислава Міци</a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="">
<div id="flexslide-block-slide1">
<a href="/en/news/pro-pidsumki-minulorichnoji-vstupnoji-kampaniji-zaprovadzhennya-.htm"><img src="/uploads/news/20250217_1247_interview_bnr.jpg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/pro-pidsumki-minulorichnoji-vstupnoji-kampaniji-zaprovadzhennya-.htm">Про підсумки минулорічної вступної кампанії, запровадження дуальної освіти, підтримку молодих вчених та волонтерського руху, низку інших питань життя УжНУ у 2025 році йшлося в інтерв’ю ректора Володимира Смоланки каналу ТБ-21</a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="flex-active-slide">
<div id="flexslide-block-slide2">
<a href="/en/news/dekanu-fizichnogo-fakultetu-doktoru-fiziko-matematichnih-nauk.htm"><img src="/uploads/news/20250215_1879_lazur-2_bnr.jpg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/dekanu-fizichnogo-fakultetu-doktoru-fiziko-matematichnih-nauk.htm">Декану фізичного факультету, доктору фізико-математичних наук, професору Володимиру Лазуру виповнилось 75! </a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="">
<div id="flexslide-block-slide3">
<a href="/en/news/Problems-of-women-in-science-were-discussed-during-the-round-tabl.htm"><img src="/uploads/news/20250212_1428_IMG_4192_(1)_bnr.jpeg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/Problems-of-women-in-science-were-discussed-during-the-round-tabl.htm">Problems of women in science were discussed during the round table ‘Challenges and opportunities for women scientists in modern conditions’</a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="">
<div id="flexslide-block-slide4">
<a href="/en/news/UzhNU-is-preparing-to-implement-a-double-degree-programme.htm"><img src="/uploads/news/20250204_1310_IMG_1589_bnr.JPG" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/UzhNU-is-preparing-to-implement-a-double-degree-programme.htm">UzhNU is preparing to implement a double degree programme with Maria Curie-Skłodowska University (Poland)</a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="">
<div id="flexslide-block-slide5">
<a href="/en/news/vid-lejtenanta-do-majora-zsu.htm"><img src="/uploads/news/20250129_1434_fa09314c-40a8-42cc-97f3-8b381ef18ecb_bnr.jpeg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/vid-lejtenanta-do-majora-zsu.htm">Від лейтенанта до майора ЗСУ: історія служби директора Центру доуніверситетської підготовки та роботи з іноземними громадянами УжНУ Владислава Міци</a></p>
</div>
</li>
<li style="width: 1200px; float: left; display: block;" class="clone">
<div id="flexslide-block-slide1">
<a href="/en/news/pro-pidsumki-minulorichnoji-vstupnoji-kampaniji-zaprovadzhennya-.htm"><img src="/uploads/news/20250217_1247_interview_bnr.jpg" alt="Банер до новини"></a><p class="flex-caption"><a href="/en/news/pro-pidsumki-minulorichnoji-vstupnoji-kampaniji-zaprovadzhennya-.htm">Про підсумки минулорічної вступної кампанії, запровадження дуальної освіти, підтримку молодих вчених та волонтерського руху, низку інших питань життя УжНУ у 2025 році йшлося в інтерв’ю ректора Володимира Смоланки каналу ТБ-21</a></p>
</div>
</li></ul></div><ol class="flex-control-nav flex-control-paging"><li><a class="">1</a></li><li><a class="flex-active">2</a></li><li><a class="">3</a></li><li><a class="">4</a></li><li><a class="">5</a></li></ol><ul class="flex-direction-nav"><li><a class="flex-prev" href="#">Previous</a></li><li><a class="flex-next" href="#">Next</a></li></ul></div>            </div>
        </div>
    </div> <!-- band front_slideshow -->

    <div class="band front_topicons">
        <div class="container">

            <div class="page_block"><div class="top_icon"><a style="background-color: #ffffff; display: inline !important;" href="/en/cat/abiturient-foreign"><img src="/uploads/root/site_icons/Books_stack_of_three.png" alt=""></a></div>
<div class="top_icon"><a href="http://e-learn.uzhnu.edu.ua/" target="_blank"> <img src="/uploads/root/site_icons/moodle_logo.png" alt=""> E-learning</a></div>
<div class="top_icon"><a href="http://dspace.uzhnu.edu.ua/" target="_blank"> <img src="/uploads/root/site_icons/dspace_logo.png" alt=""> Digital Repository</a></div>
<div class="top_icon"><a href="http://mediacenter.uzhnu.edu.ua/" target="_blank"> <img src="/uploads/root/site_icons/mediacentr_logo.png" alt=""> MediaCentre</a></div>
<div class="top_icon"><a href="http://www.erasmus.uzhnu.edu.ua/en/" target="_blank"> <img src="/uploads/root/site_icons/eu_flag.png" alt=""> Erasmus+</a></div></div>
        </div>
    </div>


    <div class="container">
        <div class="row">
            <div class="eight columns front_latestnews">
                 <!-- live feed 
                 <div class="video-container">
                  <iframe style="display: block; margin-left: auto; margin-right: auto;" src="https://www.youtube.com/embed/jbkoh2di0tw" frameborder="0" width="100%" height="240">
                  </iframe>
                 </div>
                 --> 
                                                                

    <div class="content">
        <h2>For University Entrants<a href="/en/news/cat/abiturient"><div class="readmore">More</div></a></h2><div id="yw0" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/do-uvagi-vipusknikiv-shkil---abituriyentiv-2019-roku.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20190602_1327_1138_top3_thumb_wide.png" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2019-06-22" pubdate="">22.06.2019</time>
                            <span class="hits">
                                32776                            </span>
                    </span>
                </span>
                <span>Information for university entrants 2018: Admission rules, EIT subjects, admission campaign important dates, entrant’s calculator</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/UzhNU-offers-online-training.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20181210_1960_000000000000004_thumb_wide.JPG" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2018-12-10" pubdate="">10.12.2018</time>
                            <span class="hits">
                                5941                            </span>
                    </span>
                </span>
                <span>UzhNU offers online training! Launch of new educational project at cram school of UzhNU</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>3005</span><span>4115</span></div>
</div>    </div>

                                                                        

    <div class="content">
        <h2>Science<a href="/en/news/cat/science"><div class="readmore">More</div></a></h2><div id="yw1" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/Registration-for-the-StartUp-From-Dream-to-Success-competition-i.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250127_1495_startup_thumb_wide.png" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-01-27" pubdate="">27.01.2025</time>
                            <span class="hits">
                                441                            </span>
                    </span>
                </span>
                <span>Registration for the StartUp: From Dream to Success competition is open!</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/Congratulations-to-the-teams-of-young-scientists-on-winning.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20241230_1413_20240807_1343_IMG_5183_thumb_wide.png" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2024-12-30" pubdate="">30.12.2024</time>
                            <span class="hits">
                                509                            </span>
                    </span>
                </span>
                <span>Congratulations to the teams of young scientists on winning the Competition of Scientific Projects!</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11488</span><span>11406</span></div>
</div>    </div>

                        

    <div class="content">
        <h2>Education<a href="/en/news/cat/education"><div class="readmore">More</div></a></h2><div id="yw2" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/Discussion-of-the-political-situation-in-Serbia-within-the-frame.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250204_1608_photo_2025-02-04_18-24-35_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-02-04" pubdate="">04.02.2025</time>
                            <span class="hits">
                                264                            </span>
                    </span>
                </span>
                <span>Discussion of the political situation in Serbia within the framework of the Diplomatic Front project</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/The-first-meeting-of-the-Academic-Council-in-2025-consideration.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250128_1370_IMG_1495_thumb_wide.JPG" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-01-28" pubdate="">28.01.2025</time>
                            <span class="hits">
                                1214                            </span>
                    </span>
                </span>
                <span>The first meeting of the Academic Council in 2025: consideration of a number of topical issues</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11516</span><span>11494</span></div>
</div>    </div>

                        

    <div class="content">
        <h2>International Activities<a href="/en/news/cat/irelations"><div class="readmore">More</div></a></h2><div id="yw3" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/The-delegation-of-UzhNU-completed-an-internship-at-the-University.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250204_1461_zobrazhennya_viber_2025-02-04_09-55-00-112_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-02-04" pubdate="">04.02.2025</time>
                            <span class="hits">
                                819                            </span>
                    </span>
                </span>
                <span>The delegation of UzhNU completed an internship at the University of Trnava within the framework of the Erasmus+ programme</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/The-Ambassador-Extraordinary-and-Plenipotentiary-of-Spain.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250131_1322_IMG_1563_thumb_wide.JPG" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-01-31" pubdate="">31.01.2025</time>
                            <span class="hits">
                                485                            </span>
                    </span>
                </span>
                <span>The Ambassador Extraordinary and Plenipotentiary of Spain to Ukraine Ricardo Lopez-Aranda Jagu visited UzhNU</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11514</span><span>11508</span></div>
</div>    </div>

                        

    <div class="content">
        <h2>Social activities<a href="/en/news/cat/soc_activities"><div class="readmore">More</div></a></h2><div id="yw4" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/Slovenian-writer-journalist-and-war-correspondent-Botjan-Videmek.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20250201_1963_zustrich_z_b_videmshekom_-_zagalna_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2025-02-01" pubdate="">01.02.2025</time>
                            <span class="hits">
                                350                            </span>
                    </span>
                </span>
                <span>Slovenian writer, journalist and war correspondent Boštjan Videmšek talked about peace and war in UzhNU</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/UzhNU-hosted-a-Discussion-Club-with-Slovak-MEPs-of-previous-cade.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20241017_1389_PHOTO-2024-10-17-01-56-22_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2024-10-17" pubdate="">17.10.2024</time>
                            <span class="hits">
                                805                            </span>
                    </span>
                </span>
                <span>UzhNU hosted a ‘Discussion Club’ with Slovak MEPs of previous cadences</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11510</span><span>11051</span></div>
</div>    </div>

                        

    <div class="content">
        <h2>Sport &amp; Leisure<a href="/en/news/cat/sportandleasure"><div class="readmore">More</div></a></h2><div id="yw5" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/On-the-occasion-of-the-birthday-of-their-university-students-org.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20241018_1147_dsc0761_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2024-10-18" pubdate="">18.10.2024</time>
                            <span class="hits">
                                484                            </span>
                    </span>
                </span>
                <span>On the occasion of the birthday of their university, students organised a charity fair to support the Armed Forces of Ukraine</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/This-years-Student-Autumn-was-held-online.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20201203_1056_CAT_2532_thumb_wide.JPG" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2020-12-03" pubdate="">03.12.2020</time>
                            <span class="hits">
                                3703                            </span>
                    </span>
                </span>
                <span>This year’s Student Autumn was held online</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11063</span><span>6055</span></div>
</div>    </div>

                        

    <div class="content">
        <h2>Foreign students<a href="/en/news/cat/f_students"><div class="readmore">More</div></a></h2><div id="yw6" class="list-view">
<div class="summary"></div>

<div class="items">



<div class="table"><div class="row">
<div class="col c50 left">    <article>
        <h1>
            <a href="/en/news/Diwali---a-holiday-festival-of-light-and-fire-in-UzhNU.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20241102_1022_divali_ramayan_kintsivka_zagalne_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2024-11-02" pubdate="">02.11.2024</time>
                            <span class="hits">
                                1167                            </span>
                    </span>
                </span>
                <span>Diwali - a holiday-festival of light and fire in UzhNU</span>
            </a>
        </h1>
    </article>
</div>






<div class="col c50 right">    <article>
        <h1>
            <a href="/en/news/Leaders-of-the-Student-Scientific-Society-Elected-at-Medical-Facu.htm">
                <span class="img_container">

                        <img class="thumb img_framed" src="/uploads/news/20240416_1618_IMG-2a7d_thumb_wide.jpg" alt="Мініатюра">

                    <span class="hover_panel">
                            <time class="news_date" datetime="2024-04-16" pubdate="">16.04.2024</time>
                            <span class="hits">
                                1933                            </span>
                    </span>
                </span>
                <span>Leaders of the Student Scientific Society Elected at Medical Faculty No. 2</span>
            </a>
        </h1>
    </article>
</div>
</div></div>

</div>
<div class="keys" style="display:none" title="/en/"><span>11141</span><span>10323</span></div>
</div>    </div>

                                
            </div><!-- content -->


            <div class="four columns main-sidebar">

                <!--
                <div class="sidebar ATTENTION">
                    <div class="header">
                        <a href="/uk/infocentre/ratings"></a>
                    </div>
                </div>

                <div class="sidebar ATTENTION">
                    <div class="header">
                        <a href="http://vstup.info/2016/i2016i207.html#vnz">Система "Конкурс" - УжНУ</a>
                    </div>
                </div>

                <div class="sidebar ATTENTION">
                    <div class="header">
                        <a href="http://vstup.info/2016/i2016i1153.html#vnz">Система "Конкурс" - ПГК</a>
                    </div>
                </div>
                -->

                




                                                                                <div class="round_widget news news-entrants">
    <div class="header">
        <a href="/en/news/cat/entrants_news">About University for Entrants</a><a href="/en/rss"><img id="img_icon" src="/images/icons/rss_icon.png" alt="RSS"></a>        <div class="arrow"></div>
    </div>


    <div class="content">
        <div id="yw7" class="list-view">
<div class="summary"></div>

<div class="items">


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">21</div>
                <div class="month">June</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Education-for-the-reconstruction-of-Ukraine-and-European-integra.htm">Education for the reconstruction of Ukraine and European integration: Medical Faculty No. 2</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">17</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/The-Open-Day-was-held-in-UzhNU-.htm">The Open Day was held in UzhNU </a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">27</div>
                <div class="month">July</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/13th-among-Ukrainian-universities-UzhNU-has-improved-its-position.htm">13th among Ukrainian universities: UzhNU has improved its position in the Webometrics ranking</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">26</div>
                <div class="month">July</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Uzhhorod-National-University-belongs-to-top-20-most-popular.htm">Uzhhorod National University belongs to top 20 most popular universities in Ukraine</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">14</div>
                <div class="month">September</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Rectors-video-address-to-the-first-year-students-of-UzhNU.htm">Rector’s video address to the first-year students of Uzhhorod National University</a></p>
            </div>

        </div>
    </div>

</div>
</div>
<div class="keys" style="display:none" title="/en/"><span>10679</span><span>8507</span><span>6860</span><span>6859</span><span>5799</span></div>
</div>    </div>

        <a href="/en/news/cat/entrants_news"><div class="readmore cfix">Read more</div></a>
    </div>
                                            <div class="round_widget news ">
    <div class="header">
        <a href="/en/news/">Новини УжНУ</a><a href="/en/rss"><img id="img_icon" src="/images/icons/rss_icon.png" alt="RSS"></a>        <div class="arrow"></div>
    </div>


    <div class="content">
        <div id="yw8" class="list-view">
<div class="summary"></div>

<div class="items">


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">14</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/UzhNU-is-ranked-10th-among-Ukrainian-universities-in-the-GreenMet.htm">UzhNU is ranked 10th among Ukrainian universities in the GreenMetric World University Rankings 2024</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">12</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Problems-of-women-in-science-were-discussed-during-the-round-tabl.htm">Problems of women in science were discussed during the round table ‘Challenges and opportunities for women scientists in modern conditions’</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">4</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/UzhNU-is-preparing-to-implement-a-double-degree-programme.htm">UzhNU is preparing to implement a double degree programme with Maria Curie-Skłodowska University (Poland)</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">4</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Discussion-of-the-political-situation-in-Serbia-within-the-frame.htm">Discussion of the political situation in Serbia within the framework of the Diplomatic Front project</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">4</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/The-delegation-of-UzhNU-completed-an-internship-at-the-University.htm">The delegation of UzhNU completed an internship at the University of Trnava within the framework of the Erasmus+ programme</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">1</div>
                <div class="month">February</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Slovenian-writer-journalist-and-war-correspondent-Botjan-Videmek.htm">Slovenian writer, journalist and war correspondent Boštjan Videmšek talked about peace and war in UzhNU</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">31</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/The-Ambassador-Extraordinary-and-Plenipotentiary-of-Spain.htm">The Ambassador Extraordinary and Plenipotentiary of Spain to Ukraine Ricardo Lopez-Aranda Jagu visited UzhNU</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">30</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/DRANICA24-Preserving-the-Cultural-Heritage-of-Traditional-Woodwor.htm">DRANICA.24: Preserving the Cultural Heritage of Traditional Woodworking in the Carpathian Euroregion</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">28</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/The-first-meeting-of-the-Academic-Council-in-2025-consideration.htm">The first meeting of the Academic Council in 2025: consideration of a number of topical issues</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">27</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Registration-for-the-StartUp-From-Dream-to-Success-competition-i.htm">Registration for the StartUp: From Dream to Success competition is open!</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">23</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/The-delegation-of-UzhNU-attended-the-first-transnational-reportin.htm">The delegation of UzhNU attended the first transnational reporting meeting within the framework of the grant project</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">23</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/UzhNU-results-in-the-World-University-Rankings-by-subject-2025.htm">UzhNU results in the World University Rankings by subject 2025</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">16</div>
                <div class="month">January</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/UzhNU-signed-a-partnership-agreement-on-the-implementation.htm">UzhNU signed a partnership agreement on the implementation of the Polish-Ukrainian project “Youth of the Carpathians for Eco-Smart Education”</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">30</div>
                <div class="month">December</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/Congratulations-to-the-teams-of-young-scientists-on-winning.htm">Congratulations to the teams of young scientists on winning the Competition of Scientific Projects!</a></p>
            </div>

        </div>
    </div>

</div>


<div class="anounce compact">

    <div class="table">
        <div class="row ">

            <div class="col c30 day_month">
                <div class="day">30</div>
                <div class="month">December</div>
            </div>

            <div class="col c70 borderleft">
                                <p class="item_header"><a href="/en/news/UzhNU-in-the-project-Global-Challenges-for-Universities.htm">UzhNU in the project “Global Challenges for Universities”</a></p>
            </div>

        </div>
    </div>

</div>
</div>
<div class="keys" style="display:none" title="/en/"><span>11564</span><span>11558</span><span>11517</span><span>11516</span><span>11514</span><span>11510</span><span>11508</span><span>11504</span><span>11494</span><span>11488</span><span>11476</span><span>11474</span><span>11454</span><span>11406</span><span>11405</span></div>
</div>    </div>

        <a href="/en/news/"><div class="readmore cfix">Read more</div></a>
    </div>
                                                        
                                
            </div><!-- sidebar -->
			<!-- 
            <style>
                .main-sidebar {
                    display: flex;
                    flex-direction: column;
                }

                .main-sidebar .pinned {
                    order: -1;
                }

                .pinned.round_widget.news .header {
                    background: #c47272;
                }

                .pinned.round_widget.news .header .arrow {
                    display: none;
                }
            </style>
			-->
        </div>
    </div>

</div>

<div class="band front_info_posts">
    <div class="container">
        <div class="gray_half_info top"></div>
        <div class="table">
            <div class="table-cell">
                <!--                <div class="image-round">-->
                <!--                    <img src="/uploads/news/20150303_1282_33_thumb1.jpg" id="20150303_1282_33_thumb1" />-->
                <!--                </div>-->
                <img id="info_logo" src="/images/layout/big_info.png">
            </div>
            <div class="table-cell">
                            </div>
        </div>
        <div class="gray_half_info bottom"></div>
    </div>
</div>



    
    
    <div class="band footer">
      
        <div class="footer_contact_band">
        <!--
            <i class="mega_icon fa fa-at"></i>
            <div class="container">
                <div class="table contact_us">
                    <div class="table-cell">
                        <p>Have any questions, proposals or concerns?</p>
                    </div>
                    <div class="table-cell">
                        <div id="slide_contacts_btn" class="button-menu">Contact Us<i class="fa fa-envelope-o fa-2x fa-fw"></i></div>
                    </div>
                </div>
                <div class="slide_contacts_panel">
                                    </div>
            </div>
            -->
        </div>
       


        <div class="footer_arrow"></div>

        <div class="container">
            <div class="row">
                <div class="four columns">
                    <img class="footer-brand__logo" src="/images/layout/UzNU_logo_new-header.png" alt="Логотип УжНУ">
                    <h4>Uzhhorod National University</h4>
                </div>
                <div class="eight columns">
                    <div style="overflow:hidden;">
                        <ul class="iconset social_icons">
                            <li><a class="facebook" href="https://www.facebook.com/uzhnu" target="_blank" title="Facebook">Facebook</a></li>
                            <li><a class="youtube" href="https://www.youtube.com/channel/UCSIfo-iRoeS7nf5957HnI0Q/videos" target="_blank" title="YouTube">YouTube</a></li>
                        </ul>

                        <div class="menubottom cfix">
                                                            <ul id="yw3">
<li><a href="/en/cat/general_pages/tender_commit">Public procurement</a> |</li>
<li><a href="/en/cat/general_pages/support">Site  administration</a> |</li>
<li><a href="/en/cat/general_pages/terms_of_use">Terms of use</a> |</li>
<li><a href="https://www.uzhnu.edu.ua/uk/cat/general_pages/stop_corruption">Prevention of corruption</a></li>
</ul>                                                    </div>
                    </div>
                </div>
            </div>
            <div class="row footer_partners">
                <div class="page_block"><div class="footer_partner_icon"><a href="https://mon.gov.ua/eng/" target="_blank"> <img title="Ministry of Education and Science of Ukraine" src="/uploads/root/logos/logo_MONU.svg" alt="Logo MESU"> </a></div>
<div class="footer_partner_icon"><a href="http://erasmusplus.org.ua/" target="_blank"> <img src="/uploads/root/logos/erasmus-logo_small.png" alt=""> </a></div>
<div class="footer_partner_icon"><a href="http://h2020.link/" target="_blank"> <img src="/uploads/root/logos/Horizon_2020_small.jpg" alt=""> </a></div>
<div class="footer_partner_icon"><a href="http://visegradfund.org/" target="_blank"> <img src="/uploads/root/logos/visegrad_logo_small.png" alt=""> </a></div>
<div class="footer_partner_icon"><a href="https://huskroua-cbc.eu/" target="_blank"> <img src="/uploads/root/logos/hu-sk-ro-ua.png" alt=""> </a></div>
<div class="footer_partner_icon"><a href="http://www.cost.eu/" target="_blank"> <img src="/uploads/root/logos/cost_logo_small.png" alt=""> </a></div>
<div class="footer_partner_icon"><a href="https://ro-ua.net" target="_blank"> <img src="/uploads/root/logos/logo_ro-uk_en.png" alt=""> </a></div></div>            </div>

            <div class="row">
                <div class="four columns">
                    <h4 class="case_normal">University at the map:</h4>
                    <a href="/en/cat/general_pages/contacts#map"><img class="img_framed" src="/images/uzhnu_map.gif" alt="УжНУ на мапі Ужгорода"></a>
                </div>
                <div class="eight columns">
                    <div class="text_bottom">
                        <div class="page_block"><p>Uzhhorod National University is one of the traditional universities of Ukraine accredited by the IV (highest) level of accreditation (certificate series RD - IV №0753932).</p>
<p><span>Rector – MD, Professor.;</span>Vladimir Smolanka.</p>
<h5>Contact information:</h5>
<div class="table footer-contacts-table">
<div class="row">
<div class="col c70">Administration:<br> Address: 88000, Ukraine, Transcarpathian region, Uzhhorod, Narodna Square, 3 <br> Telephone: +38 (03122) 3-33-41 <br> Fax: +38 (03122) 3-42-02 <br> E-mail: official@uzhnu.edu.ua <br><br></div>
<div class="col c30" style="border-left: thin white dotted; padding-left: 10px;">Design and development: <br><a href="/en/cat/university-it">ESI CST</a> \ Alex Dubiv<br> Webmaster: admin@uzhnu.edu.ua<br>Media: media@uzhnu.edu.ua<br> © 2020 UzhNU</div>
</div>
</div>
<!-- table --></div>                        <p>
                            </p><div style="color:#566183;">SQL час: 0 с.<br>Згенеровано за: 0.08</div>                        <p></p>
                    </div>  <!-- text_bottom -->
                    <br> 

<!-- I.UA counter <a href="http://www.i.ua/" target="_blank" onclick="this.href='http://i.ua/r.php?170712';" title="Rated by I.UA">
<script type="text/javascript" async><!--
iS='http'+(window.location.protocol=='https:'?'s':'')+
    '://r.i.ua/s?u170712&p62&n'+Math.random();
iD=document;if(!iD.cookie)iD.cookie="b=b; path=/";if(iD.cookie)iS+='&c1';
iS+='&d'+(screen.colorDepth?screen.colorDepth:screen.pixelDepth)
    +"&w"+screen.width+'&h'+screen.height;
iT=iR=iD.referrer.replace(iP=/^[a-z]*:\/\//,'');iH=window.location.href.replace(iP,'');
((iI=iT.indexOf('/'))!=-1)?(iT=iT.substring(0,iI)):(iI=iT.length);
if(iT!=iH.substring(0,iI))iS+='&f'+escape(iR);
iS+='&r'+escape(iH);
iD.write('<img src="'+iS+'" border="0" width="88" height="31" />');
</script></a> End of I.UA counter -->                </div>
            </div>
        </div>




    </div>  <!-- band footer -->



</div>
"""
for link in re.finditer(
    r"https?://[\w\-./]*",
    HTML
):
    print(link)