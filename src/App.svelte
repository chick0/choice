<script>
    import { MenuData } from './store.js';
    import { getMenus } from './storage.js';

    let menus = [];
    let selectedMenu = "";

    function updateSelectedMenu(){
        if(menus.length == 0){
            selectedMenu = "등록된 메뉴가 없습니다!";
        } else {
            // 메뉴 선택하기
            selectedMenu = menus[
                Math.floor(Math.random() * Math.floor(menus.length))
            ];
        }
    }

    MenuData.subscribe((newMenu) => {
        // 변경된 메뉴 반영하기
        menus = newMenu;
        // 메뉴 추첨하기
        updateSelectedMenu();
    });

    // 메뉴 정보 불러오기
    getMenus();
</script>

<section class="section">
    <div class="container">
        <h1 class="title is-1">메뉴</h1>
        <p class="subtitle">등록된 {menus.length}개의 메뉴중 하나를 랜덤으로 추천합니다!</p>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="content is-large">
            <blockquote>{selectedMenu}</blockquote>
        </div>
        <button
            class="button is-info is-light is-large is-fullwidth"
            on:click={updateSelectedMenu}
        >
            메뉴 추천 받기
        </button>
    </div>
</section>