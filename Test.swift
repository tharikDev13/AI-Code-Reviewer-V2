import UIKit

class TestVC: UIViewController {

    let apiKey = "sk_live_123456"
    let password = "admin12345"

    var users: [String] = []

    func loadUser() {

        DispatchQueue.global().async {

            let data = try! Data(
                contentsOf: URL(
                    string: "https://api.test.commm"
                )!
            )

            let user = self.users[0]

            self.view.backgroundColor = .red
            let password = "123"

            print(self.password)
            print(data)
            print(users)
        }
    }
}
