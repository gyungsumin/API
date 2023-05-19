creative = dict(id=None,
                name=None,
                renderingId=None,
                advertiserId=None,
                accountId=None,
                subaccountId=None,
                active=True,
                archived=False,
                version=1,
                size=dict(id=None,
                          width=0,
                          height=0,
                          iab=False,
                          kind='dfareporting#size'),
                kind='dfareporting#creative',
                lastModifiedInfo=dict(time=None),
                sslCompliant=True,
                type=None,
                sslOverride=False,
                dynamicAssetSelection=False)


class Creative:
    id = None
    # name = None
    renderingId = None
    # advertiserId = None
    # accountId = None
    subaccountId = None
    active = True
    archived = False
    version = 1

    size_id = None
    size_width = 0
    size_height = 0
    size_iab = False
    size_kind = 'dfareporting#size'

    kind = 'dfareporting#creative'
    lastModifiedInfo_time = None
    sslCompliant = True
    type = None
    sslOverride = False
    dynamicAssetSelection = False

    def __init__(self, name: str, advertiserId: int, accountId: int):
        self.name = name
        self.advertiserId = advertiserId
        self.accountId = accountId

    def generate(self):
        result = dict(id=self.id,
                      name=self.name,
                      renderingId=self.renderingId,
                      advertiserId=self.advertiserId,
                      accountId=self.accountId,
                      subaccountId=self.subaccountId,
                      active=self.active,
                      archived=self.archived,
                      version=self.version,
                      size=dict(id=self.size_id,
                                width=self.size_width,
                                height=self.size_height,
                                iab=self.size_iab,
                                kind=self.size_kind),
                      kind=self.kind,
                      lastModifiedInfo=dict(time=self.lastModifiedInfo_time),
                      sslCompliant=self.sslCompliant,
                      type=self.type,
                      sslOverride=self.sslOverride,
                      dynamicAssetSelection=self.dynamicAssetSelection)

        return result


# c = Creative(name='test', accountId=123, advertiserId=456)
# print(c.name)
# print(c.accountId)
# print(c.advertiserId)
# print(c.version)
#
# print(c.generate())
# c.name = '123'
# c.advertiserId = 5243
# c.version = 5
# print(c.name)
# print(c.advertiserId)
# print(c.version)
#
# c = c.generate()
# print(c)
