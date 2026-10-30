
import streamlit as st

# ==========================================
# 1. 페이지 설정
# ==========================================

st.set_page_config(
    page_title="MY FIT ROUTINE",
    page_icon="💪",
    layout="wide"
)


# ==========================================
# 2. 세션 상태 초기화
# ==========================================

defaults = {
    "step": 1,
    "selected_level": "초급자",
    "selected_activity": "가볍게 움직이는 편이에요",
    "routine": [],
    "generated": False,
    "sets": 2
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==========================================
# 3. CSS 디자인
# ==========================================

st.markdown("""
<style>
/* 전체 배경 및 상단 영역 */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
    background-color: #18191B !important;
}

[data-testid="stHeader"] {
    background: #18191B !important;
}

[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0;
}

/* 전체 콘텐츠 폭과 위쪽 여백 */
.block-container {
    max-width: 900px !important;
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
}

.stApp {
    color: #FFFFFF;
}

/* 상단 제목 */
.main-title {
    display: block;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
    color: #D7FF63;
    font-size: 36px;
    font-weight: 900;
    letter-spacing: 1px;
    line-height: 1.4;
    padding: 10px 0 2px 0;
    margin: 0 0 7px 0;
    overflow: visible;
}

.main-subtitle {
    display: block;
    text-align: center;
    color: #D0D2D8;
    font-size: 13px;
    letter-spacing: 1.5px;
    line-height: 1.5;
    margin: 0 0 16px 0;
}

/* 상단 구분선 간격 */
hr {
    border-color: #35363A !important;
    margin-top: 14px !important;
    margin-bottom: 18px !important;
}

/* 단계별 제목 */
.step-title {
    text-align: center;
    color: #FFFFFF;
    font-size: 29px;
    font-weight: 800;
    line-height: 1.45;
    margin: 8px auto 28px auto;
}

/* 공통 버튼 */
.stButton > button {
    border-radius: 14px;
    min-height: 55px;
    font-size: 17px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button[kind="primary"] {
    background-color: #D7FF63 !important;
    color: #18191B !important;
    border: 2px solid #D7FF63 !important;
}

.stButton > button[kind="secondary"] {
    background-color: #25262A !important;
    color: #FFFFFF !important;
    border: 1px solid #414247 !important;
}

.stButton > button:hover {
    border: 2px solid #D7FF63 !important;
}

/* 운동 레벨 영역: 중앙 정렬 + 너비 제한 */
.st-key-level_section {
    width: 100%;
    max-width: 650px;
    margin: 0 auto;
}

/* 레벨 버튼은 정사각형 */
.st-key-level_buttons div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
}

.st-key-level_buttons div[data-testid="stButton"] button {
    width: 145px !important;
    min-width: 145px !important;
    max-width: 145px !important;
    height: 145px !important;
    min-height: 145px !important;
    padding: 10px !important;
    border-radius: 20px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* 레벨 설명 */
.st-key-level_section [data-testid="stCaptionContainer"] p {
    color: #D0D2D8 !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
    text-align: center !important;
    min-height: 44px;
    overflow-wrap: break-word;
}

/* 활동 수준 영역: 너무 넓어지지 않게 제한 */
.st-key-activity_section {
    width: 100%;
    max-width: 760px;
    margin: 0 auto;
}

/* 활동 수준 선택지 사이 간격 및 줄 간격 */
.st-key-activity_section [role="radiogroup"] {
    gap: 13px !important;
}

.st-key-activity_section [role="radiogroup"] label {
    align-items: flex-start !important;
    padding: 7px 10px !important;
    border-radius: 10px;
    line-height: 1.65 !important;
}

.st-key-activity_section [role="radiogroup"] label p {
    color: #FFFFFF !important;
    font-size: 15px !important;
    white-space: normal !important;
    line-height: 1.65 !important;
}

/* 캡션 및 작은 안내 문구: 어두운 배경에서 가독성 강화 */
[data-testid="stCaptionContainer"] p,
.stMarkdown small,
small,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
.stSelectSlider label,
.stSlider label,
.stMultiSelect label,
.stSelectbox label,
.stRadio > label,
.stCheckbox label,
[data-testid="stHelp"] {
    color: #D0D2D8 !important;
    opacity: 1 !important;
}

/* 주간 운동 횟수 등 슬라이더 눈금/설명 */
[data-testid="stSlider"] *,
[data-testid="stSelectSlider"] * {
    color: #D0D2D8;
}

[data-testid="stSlider"] [data-testid="stTickBar"] *,
[data-testid="stSelectSlider"] [data-testid="stTickBar"] * {
    color: #D0D2D8 !important;
}

[data-testid="stCaptionContainer"] p {
    color: #D0D2D8 !important;
    font-size: 13px !important;
    line-height: 1.6;
}

/* 입력창 */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #25262A;
    border-color: #414247;
}

div[data-baseweb="select"] span {
    color: #FFFFFF;
}

/* 라디오 및 체크박스 */
[data-testid="stRadio"] label p,
[data-testid="stCheckbox"] label p {
    color: #FFFFFF !important;
}

/* 운동 결과 카드 */
[data-testid="stMetric"] {
    background-color: #25262A;
    padding: 18px;
    border-radius: 15px;
}

[data-testid="stMetricValue"] {
    color: #D7FF63;
}

[data-testid="stProgressBar"] > div > div {
    background-color: #D7FF63;
}

[data-testid="stAlert"] p {
    color: #FFFFFF !important;
}

/* 운동 통계 카드 제목 글씨 색상 */
[data-testid="stMetricLabel"] {
    color: #D0D2D8 !important;
    opacity: 1 !important;
}

[data-testid="stMetricLabel"] p {
    color: #D0D2D8 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* 운동 통계 카드 숫자 색상 */
[data-testid="stMetricValue"] {
    color: #D7FF63 !important;
}
/* 운동 부위 선택 태그 배경색 변경 */
[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background-color: #D7FF63 !important;
    color: #171819 !important;
    border: none !important;
}

/* 상체, 하체, 복부 글씨 색상 */
[data-testid="stMultiSelect"] [data-baseweb="tag"] span {
    color: #171819 !important;
}

/* 태그 삭제 X 버튼 색상 */
[data-testid="stMultiSelect"] [data-baseweb="tag"] svg {
    fill: #171819 !important;
    color: #171819 !important;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 4. 상단 앱 제목
# ==========================================

st.markdown("""
<div class="main-title">
    MY FIT ROUTINE
</div>

<div class="main-subtitle">
    FIND YOUR OWN WORKOUT
</div>
""", unsafe_allow_html=True)

st.markdown("---")



# ==========================================
# 5. STEP 01 운동 레벨 선택
# ==========================================

if st.session_state.step == 1:

    # 콘텐츠 전체를 하나의 Streamlit 컨테이너로 묶어
    # CSS가 실제 버튼 영역에 적용되도록 수정
    left, center, right = st.columns([1, 5, 1])

    with center:
        with st.container(key="level_section"):

            st.markdown(
                '<div class="step-title">운동 레벨을<br>선택해 주세요</div>',
                unsafe_allow_html=True
            )

            levels = [
                ("초급자", "운동이 처음이거나 루틴이 없어요"),
                ("중급자", "운동 자세를 잘 알고 나만의 루틴이 있어요"),
                ("고급자", "운동에 대한 충분한 경험과 지식이 있어요")
            ]

            # 정사각형 스타일은 레벨 선택 버튼 3개에만 적용
            with st.container(key="level_buttons"):
                cols = st.columns(3, gap="medium")

                for i, (level, description) in enumerate(levels):
                    with cols[i]:
                        selected = st.session_state.selected_level == level

                        if st.button(
                            level,
                            key=f"level_{level}",
                            type="primary" if selected else "secondary",
                            use_container_width=True
                        ):
                            st.session_state.selected_level = level
                            st.rerun()

                        st.caption(description)

            st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

            if st.button(
                "다음",
                type="primary",
                use_container_width=True,
                key="level_next"
            ):
                st.session_state.step = 2
                st.rerun()

# ==========================================
# 6. STEP 02 활동 수준 선택
# ==========================================

elif st.session_state.step == 2:

    st.markdown("""
    <div class="step-title">
        활동 수준을<br>
        선택해 주세요
    </div>
    """, unsafe_allow_html=True)

    activity_options = {
        "거의 움직이지 않아요":
            "대부분 앉아서 보내며 운동을 거의 하지 않아요",

        "가볍게 움직이는 편이에요":
            "가벼운 산책이나 출퇴근 걷기 정도를 해요",

        "보통의 사람만큼 움직여요":
            "서서 일하거나 주 2~3회 규칙적으로 운동해요",

        "몸을 꽤 많이 써요":
            "업무 중 신체 활동이 많고 에너지 소모가 커요",

        "몸을 쓰는 게 일상이에요":
            "하루 종일 고강도의 신체 활동을 지속해요"
    }

    # 활동 수준 선택 영역의 너비를 제한하고 선택지 간 간격 확보
    left, center, right = st.columns([1, 5, 1])

    with center:
        with st.container(key="activity_section"):
            activity = st.radio(
                "활동 수준",
                list(activity_options.keys()),
                key="activity_widget",
                format_func=lambda x: x + "  ·  " + activity_options[x],
                label_visibility="collapsed"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "이전",
            use_container_width=True
        ):

            st.session_state.step = 1
            st.rerun()

    with col2:

        if st.button(
            "다음",
            type="primary",
            use_container_width=True
        ):

            st.session_state.selected_activity = activity
            st.session_state.step = 3
            st.rerun()


# ==========================================
# 7. STEP 03 운동 목표 설정
# ==========================================

elif st.session_state.step == 3:

    st.markdown("""
    <div class="step-title">
        주간 운동 목표 횟수를<br>
        설정해 주세요
    </div>
    """, unsafe_allow_html=True)

    st.info("균형 잡힌 목표로 꾸준히 이어가 보세요!")

    goal = st.select_slider(
        "주간 운동 횟수",
        options=[1, 2, 3, 4, 5],
        value=3,
        format_func=lambda x: f"{x}회",
        key="goal_widget"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("추가 운동 설정")

    purpose = st.selectbox(
        "운동 목적",
        [
            "근력 증가",
            "체력 향상",
            "체중 관리",
            "자세 교정"
        ],
        key="purpose_widget"
    )

    place = st.radio(
        "운동 장소",
        ["헬스장", "집"],
        horizontal=True,
        key="place_widget"
    )

    parts = st.multiselect(
        "운동 부위",
        ["상체", "하체", "복부"],
        default=["상체", "하체", "복부"],
        key="parts_widget"
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "이전",
            use_container_width=True
        ):

            st.session_state.step = 2
            st.rerun()

    with col2:

        if st.button(
            "운동 루틴 만들기",
            type="primary",
            use_container_width=True
        ):

            if not parts:

                st.warning(
                    "운동 부위를 하나 이상 선택해 주세요."
                )

            else:

                # 선택 정보 저장
                st.session_state.purpose = purpose
                st.session_state.place = place
                st.session_state.parts = parts
                st.session_state.goal = goal

                # --------------------------
                # 운동 데이터
                # --------------------------

                workouts = {

                    "근력 증가": {
                        "헬스장": {
                            "상체": [
                                "랫 풀다운",
                                "체스트 프레스"
                            ],
                            "하체": [
                                "레그 프레스",
                                "레그 컬"
                            ],
                            "복부": [
                                "케이블 크런치",
                                "플랭크"
                            ]
                        },
                        "집": {
                            "상체": [
                                "푸쉬업",
                                "슈퍼맨"
                            ],
                            "하체": [
                                "스쿼트",
                                "런지"
                            ],
                            "복부": [
                                "플랭크",
                                "크런치"
                            ]
                        }
                    },

                    "체력 향상": {
                        "헬스장": {
                            "상체": [
                                "로잉 머신",
                                "랫 풀다운"
                            ],
                            "하체": [
                                "런닝머신",
                                "실내 자전거"
                            ],
                            "복부": [
                                "플랭크",
                                "마운틴 클라이머"
                            ]
                        },
                        "집": {
                            "상체": [
                                "암 서클",
                                "푸쉬업"
                            ],
                            "하체": [
                                "스쿼트",
                                "점핑잭"
                            ],
                            "복부": [
                                "플랭크",
                                "버드독"
                            ]
                        }
                    },

                    "체중 관리": {
                        "헬스장": {
                            "상체": [
                                "로잉 머신",
                                "체스트 프레스"
                            ],
                            "하체": [
                                "런닝머신",
                                "스쿼트"
                            ],
                            "복부": [
                                "크런치",
                                "마운틴 클라이머"
                            ]
                        },
                        "집": {
                            "상체": [
                                "푸쉬업",
                                "암 서클"
                            ],
                            "하체": [
                                "점핑잭",
                                "런지"
                            ],
                            "복부": [
                                "크런치",
                                "플랭크"
                            ]
                        }
                    },

                    "자세 교정": {
                        "헬스장": {
                            "상체": [
                                "페이스 풀",
                                "시티드 로우"
                            ],
                            "하체": [
                                "힙 어브덕션",
                                "레그 컬"
                            ],
                            "복부": [
                                "데드버그",
                                "플랭크"
                            ]
                        },
                        "집": {
                            "상체": [
                                "월 슬라이드",
                                "밴드 풀 어파트"
                            ],
                            "하체": [
                                "브릿지",
                                "버드독"
                            ],
                            "복부": [
                                "데드버그",
                                "플랭크"
                            ]
                        }
                    }
                }

                # --------------------------
                # 맞춤 루틴 생성
                # --------------------------

                result = []

                for part in parts:

                    result.extend(
                        workouts[purpose][place][part]
                    )

                st.session_state.routine = result

                # --------------------------
                # 운동 레벨별 세트 수
                # --------------------------

                if st.session_state.selected_level == "초급자":

                    st.session_state.sets = 2

                elif st.session_state.selected_level == "중급자":

                    st.session_state.sets = 3

                else:

                    st.session_state.sets = 4

                # --------------------------
                # 완료 체크 초기화
                # --------------------------

                for i in range(len(result)):

                    st.session_state[f"done_{i}"] = False

                # 결과 페이지로 이동
                st.session_state.generated = True
                st.session_state.step = 4

                st.rerun()


# ==========================================
# 8. STEP 04 운동 루틴 결과
# ==========================================

elif st.session_state.step == 4 and st.session_state.generated:

    result = st.session_state.routine
    sets = st.session_state.sets

    st.markdown("---")

    st.markdown("""
    <h2 style="
        text-align:center;
        color:#D7FF63;
        font-size:30px;
    ">
        🔥 TODAY'S WORKOUT
    </h2>
    """, unsafe_allow_html=True)

    st.caption("나에게 맞는 맞춤 운동 루틴이에요!")

    # 운동 설정 정보
    st.write(
        f"운동 레벨 : {st.session_state.selected_level}"
    )

    st.write(
        f"활동 수준 : {st.session_state.selected_activity}"
    )

    st.write(
        f"운동 목적 : {st.session_state.purpose}"
    )

    st.write(
        f"운동 장소 : {st.session_state.place}"
    )

    # --------------------------
    # 예상 운동 시간 계산
    # --------------------------

    # 준비운동 10분
    # 세트당 운동 1분
    # 세트 사이 휴식 1분
    # 운동 사이 이동 및 휴식 1분

    total_time = 10 + len(result) * (
        sets + (sets - 1) + 1
    )

    # --------------------------
    # 완료 운동 개수
    # --------------------------

    completed = sum(
        st.session_state.get(f"done_{i}", False)
        for i in range(len(result))
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "예상 운동 시간",
        f"{total_time}분"
    )

    col2.metric(
        "완료 운동",
        f"{completed}개"
    )

    col3.metric(
        "남은 운동",
        f"{len(result) - completed}개"
    )

    # --------------------------
    # 운동 진행률
    # --------------------------

    st.subheader("WORKOUT PROGRESS")

    progress = completed / len(result)

    st.progress(progress)

    st.write(
        f"현재 진행률 : {int(progress * 100)}%"
    )

    st.markdown("---")

    # --------------------------
    # 운동 체크리스트
    # --------------------------

    st.subheader("MY WORKOUT LIST")

    for i, exercise in enumerate(result):

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:

                st.write(
                    f"**{i+1:02d}  {exercise}**"
                )

                st.caption(
                    f"{sets}세트 × 10~12회"
                )

            with col2:

                st.checkbox(
                    "완료",
                    key=f"done_{i}"
                )

    # --------------------------
    # 진행률 업데이트
    # --------------------------

    completed = sum(
        st.session_state.get(f"done_{i}", False)
        for i in range(len(result))
    )

    progress = completed / len(result)

    st.progress(progress)

    st.write(
        f"운동 진행률 : {int(progress * 100)}%"
    )

    if completed == len(result):

        st.balloons()

        st.success(
            "🎉 오늘의 운동을 모두 완료했어요!"
        )

    else:

        st.info(
            f"앞으로 {len(result)-completed}개의 운동이 남았어요!"
        )

    st.warning(
        "운동 중 통증이 발생하면 중단하고 "
        "본인의 체력에 맞는 강도로 진행하세요."
    )

    st.markdown("---")

    # --------------------------
    # 이전 버튼 및 초기화
    # --------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "이전",
            use_container_width=True
        ):

            # 결과 화면과 이전 루틴 데이터 초기화
            st.session_state.generated = False
            st.session_state.routine = []

            # STEP 3으로 이동
            st.session_state.step = 3

            st.rerun()

    with col2:

        if st.button(
            "처음부터 다시 설정하기",
            type="primary",
            use_container_width=True
        ):

            # 처음 화면으로 초기화
            st.session_state.step = 1
            st.session_state.generated = False
            st.session_state.routine = []

            st.rerun()
