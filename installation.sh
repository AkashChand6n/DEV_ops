#!/bin/bash
# Made with the help of Chatgpt
# Exit immediately if a command exits with a non-zero status.
set -e

# Must be run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ Please run as root or use sudo."
   exit 1
fi

echo "📦 Updating system..."
apt update

echo "📦 Installing Java (Jenkins dependency)..."
apt install -y openjdk-17-jdk-headless

echo "🔑 Adding Jenkins GPG key and repo..."
wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list

apt update
echo "⚙️ Installing Jenkins..."
apt install -y jenkins

echo "🔧 Giving Jenkins user access to Docker..."
usermod -aG docker jenkins
chown root:docker /var/run/docker.sock

echo "🔓 Granting sudo access to Jenkins user..."
echo "jenkins ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jenkins
chmod 440 /etc/sudoers.d/jenkins

echo "🐳 Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
rm get-docker.sh

echo "☸️ Setting up Kubernetes (k8s)..."

cat <<EOF > /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter

cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sysctl --system

swapoff -a
(crontab -l 2>/dev/null; echo "@reboot /sbin/swapoff -a") | crontab - || true

apt-get update -y
apt-get install -y software-properties-common gpg curl apt-transport-https ca-certificates

echo "📦 Installing CRI-O runtime..."
mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/addons:/cri-o:/prerelease:/main/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/cri-o-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/cri-o-apt-keyring.gpg] https://pkgs.k8s.io/addons:/cri-o:/prerelease:/main/deb/ /" > /etc/apt/sources.list.d/cri-o.list
apt-get update -y
apt-get install -y cri-o
systemctl daemon-reload
systemctl enable crio --now
systemctl start crio.service

echo "📦 Installing crictl..."
VERSION="v1.30.0"
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$VERSION-linux-amd64.tar.gz

echo "📦 Installing kubelet, kubeadm, and kubectl..."
KUBERNETES_VERSION=1.30
curl -fsSL https://pkgs.k8s.io/core:/stable:/v$KUBERNETES_VERSION/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v$KUBERNETES_VERSION/deb/ /" > /etc/apt/sources.list.d/kubernetes.list
apt-get update -y
apt-get install -y kubelet kubeadm kubectl

echo "✅ Setup complete! Jenkins, Docker, and Kubernetes are installed and configured."
