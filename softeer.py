'''
문자열 패턴은 소문자 알파벳으로만 이루어져 있으며,
문자열을 이루고 있는 문자들은 항상 연속해서 k개 이상 등장해야 합니다.
예를 들어 k = 3일 때,
문자열 "abbbaaa"는 맨 앞에 있는 a가 연속해서3번 이상 등장하지 않았기에
올바른 문자열 패턴이 아니지만,
문자열 "aaaaadddbbbaaa"는 올바른 문자열 패턴이 됩니다.
수고를 덜기 위해 초기에 그려져 있던 디자인 패턴을 토대로
가장 적은 알파벳 변경을 통해 원하는 패턴을 만들고자 합니다.
초기 디자인 패턴에 해당하는 길이가 n인 문자열 S가 주어졌을 때,
알파벳을 최소로 바꿔서 각 알파벳이 항상 연속해서 k개 이상씩 등장하도록 만드는
프로그램을 작성해 보세요.

1 <= k <= n <= 2000

첫번째 줄에는 n과 k가 공백을 사이에 두고 주어집니다.
두번째 줄에는 문자열 S가 주어집니다.
문자열 S는 소문자 알파벳으로만 이루어져 있습니다.

조건을 만족시키기 위해 바꿔야 하는 최소 알파벳의 수를 출력합니다.
'''

'''
입력
6 2
aabccb
출력
2

입력
7 3
adcbbbb
출력
2
'''