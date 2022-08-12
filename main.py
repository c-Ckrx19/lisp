from postgres13 import MyPostgres


def main():
    tst_post = MyPostgres()
    tst_post.connect()
    tst_post.tst_conn()


if __name__ == '__main__':
    main()
